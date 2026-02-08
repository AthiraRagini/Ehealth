from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_login(request):
    """Redirect /accounts/login/ to patient login"""
    return redirect('patient_login')

urlpatterns = [
 
    path('accounts/login/', redirect_to_login, name='accounts_login'),
    
   
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('singleblog/', views.singleblog, name='singleblog'),
    path('department/', views.department, name='department'),
    path('elements/', views.elements, name='elements'),

    path('doctor/login/', views.doctor_login, name='doctor_login'),
    path('doctor/register/', views.doctor_register, name='doctor_register'),
    path('doctor/home/', views.doctor_home, name='doctor_home'),
    path('doctor/patients/', views.doctor_patients, name='doctor_patients'),
    # Removed patient assignment accept/reject URLs (feature reverted)
    path('doctor/patient/<int:patient_id>/health-data/', views.doctor_patient_health_data, name='doctor_patient_health_data'),
    path('doctor/health-data/<int:health_data_id>/edit/', views.doctor_edit_health_data, name='doctor_edit_health_data'),
    path('doctor/appointments/', views.doctor_appointments, name='doctor_appointments'),
    path('doctor/appointment/<int:appointment_id>/accept/', views.doctor_accept_appointment, name='doctor_accept_appointment'),
    path('doctor/appointment/<int:appointment_id>/reject/', views.doctor_reject_appointment, name='doctor_reject_appointment'),

   
    path('patient/login/', views.patient_login, name='patient_login'),
    path('patient/register/', views.patient_register, name='patient_register'),
    path('patient/home/', views.patient_home, name='patient_home'),
    path('patient/health-data/', views.patient_health_data, name='patient_health_data'),
    path('patient/book-appointment/', views.patient_book_appointment, name='patient_book_appointment'),
    path('patient/my-appointments/', views.patient_my_appointments, name='patient_my_appointments'),
    path('patient/appointment/<int:appointment_id>/pay/', views.patient_pay_fee, name='patient_pay_fee'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('patient/appointment/<int:appointment_id>/pay/pin/', views.patient_pay_pin, name='patient_pay_pin'),

 
    path('admin/home/', views.admin_home, name='admin_home'),
    path('admin/users/', views.admin_users, name='admin_users'),
    path('admin/patients/', views.admin_patients, name='admin_patients'),
    path('admin/doctors/', views.admin_doctors, name='admin_doctors'),

    path('admin/appointments/', views.admin_appointments, name='admin_appointments'),
    path('admin/payments/', views.admin_payments, name='admin_payments'),
    path('admin/doctor/<int:doctor_id>/edit/', views.admin_edit_doctor, name='admin_edit_doctor'),
    path('admin/patient/<int:patient_id>/edit/', views.admin_edit_patient, name='admin_edit_patient'),
    path('doctor/profile/edit/', views.doctor_profile_edit, name='doctor_profile_edit'),
    path('admin/doctor/<int:doctor_id>/edit/', views.admin_edit_doctor, name='admin_edit_doctor'),
    path('doctor/profile/edit/', views.doctor_profile_edit, name='doctor_profile_edit'),
    path('deletedoctor/<int:doctor_id>/', views.deletedoctor, name='deletedoctor'),
    path('deletepatient/<int:patient_id>/', views.deletepatient, name='deletepatient'),
    path('admin/patient/<int:patient_id>/', views.admin_view_health_data, name='admin_view_health_data'),
    #additional
    path('doctor/prescription_add/<int:appointment_id>/',views.doctor_add_prescription,name='doctor_add_prescription'),
    path('doctor/video-call/<int:appointment_id>/',views.doctor_video_call,name='doctor_video_call'),
    path('patient/video-call/<int:appointment_id>/', views.patient_video_call, name='patient_video_call'),
    path('patient/alerts/', views.patient_health_alerts, name='patient_alerts'),
   

    path('logout/', views.logout_view, name='logout'),
]

