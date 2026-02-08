from django.contrib import admin
from .models import Doctor, Patient, Appointment, HealthData, Payment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialization', 'phone', 'fee']
    list_filter = ['specialization']
    search_fields = ['user__username', 'user__email', 'specialization']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'phone', 'assigned_doctor']
    list_filter = ['assigned_doctor']
    search_fields = ['user__username', 'user__email', 'phone']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time', 'status']
    list_filter = ['status', 'date', 'doctor']
    search_fields = ['patient__user__username', 'doctor__user__username']
    date_hierarchy = 'date'

@admin.register(HealthData)
class HealthDataAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date', 'blood_pressure', 'sugar', 'pse', 'weight']
    list_filter = ['date']
    search_fields = ['patient__user__username']
    date_hierarchy = 'date'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'amount', 'status', 'payment_date']
    list_filter = ['status', 'payment_date']
    search_fields = ['patient__user__username', 'doctor__user__username', 'transaction_id']
    date_hierarchy = 'payment_date'
