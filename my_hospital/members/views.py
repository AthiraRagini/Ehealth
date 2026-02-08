from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from django.db.models import Q, Sum, Prefetch
from functools import wraps
from .models import Doctor, Patient, Appointment, HealthData, Payment
from .forms import HealthForm, AppointmentForm, PaymentForm, UserRegisterForm, DoctorRegisterForm, AdminPatientEditForm, PaymentGatewayForm
from .forms import PinForm
from .forms import DoctorRegisterForm
import uuid
from django.contrib import messages

def patient_required(view_func):
    """Decorator to ensure user is a patient"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('patient_login')
        try:
            Patient.objects.get(user=request.user)
            return view_func(request, *args, **kwargs)
        except Patient.DoesNotExist:
            return redirect('index')
    return wrapper

def doctor_required(view_func):
    """Decorator to ensure user is a doctor"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('doctor_login')
        try:
            Doctor.objects.get(user=request.user)
            return view_func(request, *args, **kwargs)
        except Doctor.DoesNotExist:
            return redirect('index')
    return wrapper


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def singleblog(request):
    return render(request, 'singleblog.html')

def department(request):
   
    departments = Doctor.objects.exclude(specialization='').values_list('specialization', flat=True).distinct()
  
    doctors_by_dept = {}
    for dept in departments:
        doctors_by_dept[dept] = Doctor.objects.filter(specialization=dept).select_related('user')
    
 
    common_departments = ['Eye Care', 'Skin Care', 'Pathology', 'Medicine', 'Dental', 'Cardiology', 'Neurology', 'Orthopedics']
    
    context = {
        'departments': departments if departments else common_departments,
        'doctors_by_dept': doctors_by_dept,
    }
    return render(request, 'department.html', context)

def elements(request):
    return render(request, 'elements.html')


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                doctor = Doctor.objects.get(user=user)
                login(request, user)
                next_url = request.GET.get('next', 'doctor_home')
                return redirect(next_url)
            except Doctor.DoesNotExist:
                return render(request, 'doctor_login.html', {'error': 'Not a doctor account'})
        else:
            return render(request, 'doctor_login.html', {'error': 'Invalid credentials'})
    return render(request, 'doctor_login.html')

def doctor_register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        doctor_form = DoctorRegisterForm(request.POST)
        if not user_form.is_valid() or not doctor_form.is_valid():
            errors = []
            if not user_form.is_valid():
                errors += [v for k, v in user_form.errors.items()]
            if not doctor_form.is_valid():
                errors += [v for k, v in doctor_form.errors.items()]
            return render(request, 'doctor_register.html', {'error': ' '.join(str(e) for e in errors), 'user_form': user_form, 'doctor_form': doctor_form})
        
        username = user_form.cleaned_data['username']
        email = user_form.cleaned_data['email']
        password = user_form.cleaned_data['password']
        
        if User.objects.filter(username=username).exists():
            return render(request, 'doctor_register.html', {'error': 'Username already exists', 'user_form': user_form, 'doctor_form': doctor_form})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        doctor = doctor_form.save(commit=False)
        doctor.user = user
        doctor.save()
        return redirect('doctor_login')
    else:
        user_form = UserRegisterForm()
        doctor_form = DoctorRegisterForm()
    return render(request, 'doctor_register.html', {'user_form': user_form, 'doctor_form': doctor_form})

@doctor_required
def doctor_home(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')
    
    assigned_patients = Patient.objects.filter(assigned_doctor=doctor)
    appointments = Appointment.objects.filter(doctor=doctor).order_by('-date', '-time')
    
    context = {
        'doctor': doctor,
        'assigned_patients': assigned_patients,
        'appointments': appointments,
    }
    return render(request, 'doctor_home.html', context)

@doctor_required
def doctor_patients(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')
    
    patients = Patient.objects.filter(assigned_doctor=doctor)
    context = {
        'doctor': doctor,
        'patients': patients,
    }
    return render(request, 'doctor_patients.html', context)
@doctor_required
def doctor_patient_health_data(request, patient_id):
    """
    NOTE: We intentionally do NOT filter by assigned_doctor here to avoid 404
    if the patient exists but isn't yet assigned. Access control for editing
    still enforced elsewhere (e.g., doctor_edit_health_data).
    """
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')

    patient = get_object_or_404(Patient, id=patient_id)
    
    health_data_list = HealthData.objects.filter(patient=patient).order_by('-date', '-updated_at')
    
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.patient = patient
            health_data.save()
            return redirect('doctor_patient_health_data', patient_id=patient_id)
    else:
        form = HealthForm()
    
    context = {
        'doctor': doctor,
        'patient': patient,
        'form': form,
        'health_data_list': health_data_list,
    }
    return render(request, 'doctor_patient_health_data.html', context)

@doctor_required
def doctor_edit_health_data(request, health_data_id):
    try:
        doctor = Doctor.objects.get(user=request.user)
        health_data = get_object_or_404(HealthData, id=health_data_id)
        
       
        if health_data.patient.assigned_doctor != doctor:
            return redirect('doctor_home')
    except Doctor.DoesNotExist:
        return redirect('index')
    
    if request.method == 'POST':
        form = HealthForm(request.POST, instance=health_data)
        if form.is_valid():
            form.save()
            return redirect('doctor_patient_health_data', patient_id=health_data.patient.id)
    else:
        form = HealthForm(instance=health_data)
    
    context = {
        'doctor': doctor,
        'health_data': health_data,
        'form': form,
    }
    return render(request, 'doctor_edit_health_data.html', context)

# @doctor_required
# def doctor_appointments(request):
#     try:
#         doctor = Doctor.objects.get(user=request.user)
#     except Doctor.DoesNotExist:
#         return redirect('index')
    
#     appointments = Appointment.objects.filter(doctor=doctor).order_by('-date', '-time')
#     context = {
#         'doctor': doctor,
#         'appointments': appointments,
#     }
#     return render(request, 'doctor_appointments.html', context)


#additional
@doctor_required
def doctor_appointments(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')
    
    appointments = Appointment.objects.filter(
        doctor=doctor
    ).prefetch_related('payments').order_by('-date', '-time')

    # 🔹 Add helper attributes for template use
    for appointment in appointments:
        appointment.is_paid = appointment.payments.filter(status='paid').exists()
        appointment.has_prescription = hasattr(appointment, 'prescription')

    context = {
        'doctor': doctor,
        'appointments': appointments,
    }
    return render(request, 'doctor_appointments.html', context)


@doctor_required
def doctor_accept_appointment(request, appointment_id):
    """Mark a pending appointment as accepted (confirmed) by the doctor."""
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')

    try:
        appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor)
    except Exception:
        messages.error(request, 'Appointment not found or not assigned to you.')
        return redirect('doctor_appointments')

    if request.method != 'POST':
        return redirect('doctor_appointments')

    if appointment.status == 'pending':
        appointment.status = 'confirmed'
        appointment.save()
        messages.success(request, 'Appointment accepted.')
    else:
        messages.info(request, f'Appointment already {appointment.get_status_display()}')
    return redirect('doctor_appointments')


@doctor_required
def doctor_reject_appointment(request, appointment_id):
    """Mark a pending appointment as rejected by the doctor."""
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('index')

    try:
        appointment = get_object_or_404(Appointment, id=appointment_id, doctor=doctor)
    except Exception:
        messages.error(request, 'Appointment not found or not assigned to you.')
        return redirect('doctor_appointments')

    if request.method != 'POST':
        return redirect('doctor_appointments')

    if appointment.status == 'pending':
        appointment.status = 'rejected'
        appointment.save()
        messages.success(request, 'Appointment rejected.')
    else:
        messages.info(request, f'Appointment already {appointment.get_status_display()}')
    return redirect('doctor_appointments')


 




def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                patient = Patient.objects.get(user=user)
                login(request, user)
                next_url = request.GET.get('next', 'patient_home')
                return redirect(next_url)
            except Patient.DoesNotExist:
                return render(request, 'patient_login.html', {'error': 'Not a patient account'})
        else:
            return render(request, 'patient_login.html', {'error': 'Invalid credentials'})
    return render(request, 'patient_login.html')


def admin_login(request):
    """Custom admin login page for staff users (styled like other auth pages)."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active and user.is_staff:
                login(request, user)
                next_url = request.GET.get('next', 'admin_home')
                return redirect(next_url)
            else:
                return render(request, 'admin_login.html', {'error': 'Not an admin/staff account'})
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'admin_login.html')

def patient_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        phone = request.POST.get('phone', '')
        
        if User.objects.filter(username=username).exists():
            return render(request, 'patient_register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        Patient.objects.create(user=user, age=age, phone=phone)
        return redirect('patient_login')
    return render(request, 'patient_register.html')

@patient_required
def patient_home(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        return redirect('index')
    
    context = {
        'patient': patient,
    }
    return render(request, 'patient_home.html', context)

from .utils import generate_health_alerts

@patient_required
def patient_health_data(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        return redirect('index')
    
    health_data_list = HealthData.objects.filter(
        patient=patient
    ).order_by('-date', '-updated_at')
    
    if request.method == 'POST':
        form = HealthForm(request.POST)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.patient = patient
            health_data.save()

            # 👇 alert logic (safe)
            doctor = getattr(patient, 'doctor', None)
            generate_health_alerts(patient, doctor, health_data)

            return redirect('patient_health_data')
    else:
        form = HealthForm()
    
    context = {
        'patient': patient,
        'form': form,
        'health_data_list': health_data_list,
    }
    return render(request, 'patient_health.html', context)


@patient_required
def patient_book_appointment(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        return redirect('index')
    
    specialization = request.GET.get('specialization', '')
    search_query = request.GET.get('search', '')
    
    
    doctors = Doctor.objects.select_related('user').all()
    
    
    if specialization:
        doctors = doctors.filter(specialization__icontains=specialization)
    
    if search_query:
        doctors = doctors.filter(
            Q(user__username__icontains=search_query) |
            Q(user__first_name__icontains=search_query) |
            Q(user__last_name__icontains=search_query) |
            Q(specialization__icontains=search_query)
        )
    
    all_specializations = Doctor.objects.exclude(specialization='').values_list('specialization', flat=True).distinct()
    
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        if not doctor_id:
            context = {
                'patient': patient,
                'doctors': doctors,
                'all_specializations': all_specializations,
                'selected_specialization': specialization,
                'search_query': search_query,
                'error': 'Please select a doctor.'
            }
            return render(request, 'patient_book_appointment.html', context)
        
        date = request.POST.get('date')
        time = request.POST.get('time')
        description = request.POST.get('description', '')
        
        doctor = get_object_or_404(Doctor, id=doctor_id)
        appointment = Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            date=date,
            time=time,
            description=description
        )
        
        Payment.objects.create(
            appointment=appointment,
            patient=patient,
            doctor=doctor,
            amount=doctor.fee or 0,
            status='pending'
        )

        patient.assigned_doctor = doctor
        patient.save()
        
        return redirect('patient_my_appointments')
    
    context = {
        'patient': patient,
        'doctors': doctors,
        'all_specializations': all_specializations,
        'selected_specialization': specialization,
        'search_query': search_query,
    }
    return render(request, 'patient_book_appointment.html', context)

# @patient_required
# def patient_my_appointments(request):
#     try:
#         patient = Patient.objects.get(user=request.user)
#     except Patient.DoesNotExist:
#         return redirect('index')
    
#     appointments = Appointment.objects.filter(patient=patient).order_by('-date', '-time')
#     context = {
#         'patient': patient,
#         'appointments': appointments,
#     }
#     return render(request, 'patient_my_appointments.html', context)

#additional
@login_required
def patient_my_appointments(request):
    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        return redirect('index')
    
    appointments = Appointment.objects.filter(patient=patient).prefetch_related('payments').order_by('-date', '-time')

    # 🔹 Add a helper attribute for video call eligibility
    for appointment in appointments:
        appointment.is_paid = appointment.payments.filter(status='paid').exists()

    context = {
        'patient': patient,
        'appointments': appointments,
    }
    return render(request, 'patient_my_appointments.html', context)

@patient_required
def patient_pay_fee(request, appointment_id):
    try:
        patient = Patient.objects.get(user=request.user)
        appointment = get_object_or_404(Appointment, id=appointment_id, patient=patient)
    except Patient.DoesNotExist:
        return redirect('index')
    
    try:
        payment = Payment.objects.get(appointment=appointment)
    except Payment.DoesNotExist:
        payment = Payment.objects.create(
            appointment=appointment,
            patient=patient,
            doctor=appointment.doctor,
            amount=appointment.doctor.fee,
            status='pending'
        )
    
    if request.method == 'POST':
       
        gateway_form = PaymentGatewayForm(request.POST)
        if gateway_form.is_valid():
            
            request.session['pending_payment_id'] = payment.id
           
            cardnum = gateway_form.cleaned_data.get('card_number', '')
            request.session['pending_card_last4'] = cardnum[-4:] if cardnum else ''
            messages.info(request, 'Proceed to PIN entry to complete payment')
            return redirect('patient_pay_pin', appointment_id=appointment_id)
        else:
         
            messages.error(request, 'Invalid card information — please check the highlighted fields')
    else:
        gateway_form = PaymentGatewayForm()
    
    context = {
        'patient': patient,
        'appointment': appointment,
        'payment': payment,
        'gateway_form': gateway_form,
    }
    return render(request, 'patient_pay_fee.html', context)

@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_home(request):
    total_users = User.objects.count()
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    total_payments = Payment.objects.count()
    total_revenue = Payment.objects.filter(status='paid').aggregate(
        total=Sum('amount')
    )['total'] or 0
    
    recent_appointments = Appointment.objects.all().order_by('-created_at')[:10]
    recent_payments = Payment.objects.all().order_by('-payment_date')[:10]
    
    context = {
        'total_users': total_users,
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'total_payments': total_payments,
        'total_revenue': total_revenue,
        'recent_appointments': recent_appointments,
        'recent_payments': recent_payments,
    }
    return render(request, 'admin_home.html', context)

@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_users(request):
    users = User.objects.all().order_by('-date_joined')
    
    patients = Patient.objects.select_related('user', 'assigned_doctor').prefetch_related(
        Prefetch('healthdata_set', queryset=HealthData.objects.order_by('-updated_at', '-date'), to_attr='health_list')
    ).all()
    doctors = Doctor.objects.select_related('user').all()
    
    patient_assigned_map = {p.user_id: p.assigned_doctor for p in patients}
    doctor_patient_counts = {d.user_id: d.patients.count() for d in doctors}
    

    for u in users:
        u.assigned_doctor_display = None
        u.assigned_patients_count = 0
        try:
            patient = u.patient
            if patient.assigned_doctor:
                u.assigned_doctor_display = patient.assigned_doctor.user.get_full_name() or patient.assigned_doctor.user.username
        except Patient.DoesNotExist:
            pass
        try:
            doctor_obj = u.doctor
            u.assigned_patients_count = doctor_obj.patients.count()
        except Doctor.DoesNotExist:
            pass

    context = {
        'users': users,
        'patients': patients,
        'doctors': doctors,
    }
    return render(request, 'admin_users.html', context)


@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_patients(request):
    """Admin: show all patients in a separate page."""
    patients = Patient.objects.select_related('user', 'assigned_doctor').all().order_by('-id')
    context = {
        'patients': patients,
    }
    return render(request, 'admin_patients.html', context)


@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_doctors(request):
    """Admin: show all doctors in a separate page."""
    doctors = Doctor.objects.select_related('user').all().order_by('-id')
    context = {
        'doctors': doctors,
    }
    return render(request, 'admin_doctors.html', context)




@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = AdminPatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = AdminPatientEditForm(instance=patient)
    context = {'patient': patient, 'form': form}
    return render(request, 'admin_edit_patient.html', context)


@staff_member_required
  


@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    else:
        form = DoctorRegisterForm(instance=doctor)
    context = {'doctor': doctor, 'form': form}
    return render(request, 'admin_edit_doctor.html', context)


# @doctor_required
# def doctor_profile_edit(request):
#     try:
#         doctor = Doctor.objects.get(user=request.user)
#     except Doctor.DoesNotExist:
#         return redirect('doctor_register')

#     if request.method == 'POST':
#         form = DoctorRegisterForm(request.POST, instance=doctor)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor_home')
#     else:
#         form = DoctorRegisterForm(instance=doctor)
#     return render(request, 'doctor_profile_edit.html', {'form': form, 'doctor': doctor})

#additional
@doctor_required
def doctor_profile_edit(request):
    try:
        doctor = Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        return redirect('doctor_register')

    if request.method == 'POST':
        form = DoctorRegisterForm(request.POST, instance=doctor)
        if form.is_valid():
            doctor = form.save(commit=False)
            # save email to User model
            request.user.email = form.cleaned_data['email']
            request.user.save()
            doctor.save()
            return redirect('doctor_home')
    else:
        # prefill email from user
        initial_data = {'email': request.user.email}
        form = DoctorRegisterForm(instance=doctor, initial=initial_data)

    return render(request, 'doctor_profile_edit.html', {'form': form, 'doctor': doctor})


@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_appointments(request):
    appointments = Appointment.objects.all().order_by('-date', '-time')
    context = {
        'appointments': appointments,
    }
    return render(request, 'admin_appointments.html', context)

@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_payments(request):
    payments = Payment.objects.all().order_by('-payment_date')
    context = {
        'payments': payments,
    }
    return render(request, 'admin_payments.html', context)


@patient_required
def patient_pay_pin(request, appointment_id):
    try:
        patient = Patient.objects.get(user=request.user)
        appointment = get_object_or_404(Appointment, id=appointment_id, patient=patient)
    except Patient.DoesNotExist:
        return redirect('index')

    
    pending_id = request.session.get('pending_payment_id')
    if not pending_id:
        messages.error(request, 'Card entry step not completed — please enter payment details first.')
        return redirect('patient_pay_fee', appointment_id=appointment_id)

    payment = get_object_or_404(Payment, id=pending_id, appointment=appointment)

    if request.method == 'POST':
        form = PinForm(request.POST)
        if form.is_valid():
            
            transaction_id = uuid.uuid4().hex[:12].upper()
            payment.transaction_id = transaction_id
            payment.status = 'paid'
            payment.save()
            appointment.status = 'confirmed'
            appointment.save()
           
            request.session.pop('pending_payment_id', None)
            request.session.pop('pending_card_last4', None)
            messages.success(request, f'Payment successful. Transaction ID: {transaction_id}')
            return redirect('patient_my_appointments')
    else:
        form = PinForm()

    context = {
        'patient': patient,
        'appointment': appointment,
        'payment': payment,
        'form': form,
        'card_last4': request.session.get('pending_card_last4', ''),
    }
    return render(request, 'patient_pay_pin.html', context)

def deletedoctor(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    doctor.delete()
    return redirect('admin_users')
def deletepatient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    return redirect('admin_users')
@staff_member_required
@staff_member_required(login_url='/admin/login/')
def admin_view_health_data(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    health_data_list = HealthData.objects.filter(patient=patient).order_by('-date')
    return render(request, 'admin_view_health_data.html', {
        'patient': patient,
        'health_data_list': health_data_list
    })


# -
def logout_view(request):
    logout(request)
    return redirect('index')
######################## additional

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Appointment, Prescription

@login_required
def doctor_add_prescription(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Try to fetch existing prescription
    try:
        prescription = Prescription.objects.get(appointment=appointment)
    except Prescription.DoesNotExist:
        prescription = None

    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        medicines = request.POST.get('medicines')
        doctor_notes = request.POST.get('doctor_notes')
        report_file = request.FILES.get('report_file')

        if prescription:
            # UPDATE
            prescription.diagnosis = diagnosis
            prescription.medicines = medicines
            prescription.doctor_notes = doctor_notes
            if report_file:
                prescription.report_file = report_file
            prescription.save()
        else:
            # CREATE
            Prescription.objects.create(
                appointment=appointment,
                patient=appointment.patient,
                doctor=appointment.doctor,
                diagnosis=diagnosis,
                medicines=medicines,
                doctor_notes=doctor_notes,
                report_file=report_file
            )

        return redirect('doctor_appointments')

    return render(request, 'doctor_add_prescription.html', {
        'appointment': appointment,
        'prescription': prescription
    })


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .zoom_utils import create_zoom_meeting

# @login_required
# def doctor_video_call(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)

#     # Only allow the doctor of this appointment
#     if request.user != appointment.doctor.user:
#         messages.error(request, "You are not allowed to join this meeting.")
#         return redirect('doctor_home')  # must exist in urls.py

#     # Create Zoom meeting if it doesn't exist
#     if not appointment.zoom_meeting_id:
#         try:
#             topic = f"Appointment with {appointment.patient.user.get_full_name()}"
#             zoom_meeting = create_zoom_meeting(topic)

#             # Save meeting info in DB
#             appointment.zoom_meeting_id = zoom_meeting.get('id')
#             appointment.zoom_join_url = zoom_meeting.get('join_url')
#             appointment.zoom_start_url = zoom_meeting.get('start_url')  # for doctor
#             appointment.save()
#             print("Zoom meeting created:", zoom_meeting)  # debug

#         except Exception as e:
#             # Show error message and redirect
#             messages.error(request, f"Failed to create Zoom meeting: {e}")
#             return redirect('doctor_home')

#     return render(request, 'video_call.html', {
#         'appointment': appointment,
#         'start_url': appointment.zoom_start_url  # doctor uses this link
#     })

@login_required
def doctor_video_call(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)

    if request.user != appointment.doctor.user:
        messages.error(request, "You are not allowed.")
        return redirect('doctor_home')

    try:
        topic = f"Appointment with {appointment.patient.user.get_full_name()}"

        # ✅ Always generate fresh Zoom data
        zoom_meeting = create_zoom_meeting(topic)

        appointment.zoom_meeting_id = zoom_meeting['id']
        appointment.zoom_join_url = zoom_meeting['join_url']
        appointment.zoom_start_url = zoom_meeting['start_url']
        appointment.save()

        # 🚀 Redirect directly to Zoom (BEST UX)
        return redirect(appointment.zoom_start_url)

    except Exception as e:
        messages.error(request, f"Zoom error: {e}")
        return redirect('doctor_home')




from django.shortcuts import render, get_object_or_404
from .models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def patient_video_call(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, patient__user=request.user)

    if appointment.status != 'confirmed' or not appointment.payments.filter(status='paid').exists():
        return render(request, 'error.html', {'message': 'Video call not allowed.'})

    # Create or retrieve Zoom meeting for this appointment
    topic = f"Appointment with Dr. {appointment.doctor.user.get_full_name()}"
    zoom_meeting = create_zoom_meeting(topic)

    join_url = zoom_meeting.get('join_url')

    return render(request, 'patient_video_call.html', {
        'appointment': appointment,
        'join_url': join_url
    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HealthAlert, Patient

@patient_required
def patient_health_alerts(request):
    patient = Patient.objects.get(user=request.user)
    alerts = HealthAlert.objects.filter(patient=patient).order_by('-created_at')

    return render(request, 'alerts.html', {
        'alerts': alerts
    })




