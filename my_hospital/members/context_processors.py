from django.db.models import Sum
from django.utils import timezone
from django.db.models.functions import TruncDate
from django.contrib.auth import get_user_model

from .models import Patient, Doctor, Appointment, Payment


def admin_stats(request):
    """Provide admin dashboard counts to templates for staff users only."""
    if not request.user.is_authenticated or not request.user.is_staff:
        return {}

    User = get_user_model()
    total_users = User.objects.count()
    total_patients = Patient.objects.count()
    total_doctors = Doctor.objects.count()
    total_appointments = Appointment.objects.count()
    pending_appointments = Appointment.objects.filter(status='pending').count()
    total_payments = Payment.objects.count()
    pending_payments = Payment.objects.filter(status='pending').count()
    revenue_agg = Payment.objects.filter(status='paid').aggregate(total=Sum('amount'))
    total_revenue = revenue_agg.get('total') or 0
    # revenue for the last 7 days
    today = timezone.now().date()
    start_date = today - timezone.timedelta(days=6)
    revenue_qs = (
        Payment.objects.filter(status='paid', payment_date__date__gte=start_date)
        .annotate(day=TruncDate('payment_date'))
        .values('day')
        .annotate(total=Sum('amount'))
        .order_by('day')
    )
    # Make a dictionary for quick lookup
    revenue_map = {r['day'].isoformat(): float(r['total'] or 0) for r in revenue_qs}
    labels = []
    data = []
    for i in range(7):
        d = start_date + timezone.timedelta(days=i)
        labels.append(d.strftime('%b %d'))
        data.append(revenue_map.get(d.isoformat(), 0))
    recent_appointments = Appointment.objects.all().order_by('-created_at')[:10]
    recent_payments = Payment.objects.all().order_by('-payment_date')[:10]

    return {
        'admin_total_users': total_users,
        'admin_total_patients': total_patients,
        'admin_total_doctors': total_doctors,
        'admin_total_appointments': total_appointments,
        'admin_pending_appointments': pending_appointments,
        'admin_total_payments': total_payments,
        'admin_pending_payments': pending_payments,
        'admin_total_revenue': total_revenue,
        'recent_appointments': recent_appointments,
        'recent_payments': recent_payments,
        'admin_revenue_labels': labels,
        'admin_revenue_data': data,
        # also provide older style names for compatibility
        'total_users': total_users,
        'total_patients': total_patients,
        'total_doctors': total_doctors,
        'total_appointments': total_appointments,
        'total_payments': total_payments,
        'total_revenue': total_revenue,
    }
