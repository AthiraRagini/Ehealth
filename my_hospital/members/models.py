from django.db import models
from django.contrib.auth.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    assigned_doctor = models.ForeignKey('Doctor', on_delete=models.SET_NULL, null=True, blank=True, related_name='patients')
    # assigned_doctor field present

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('rejected', 'Rejected'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    # 🔹 Zoom Video Call fields (ADD THESE)
    # zoom_meeting_id = models.CharField(max_length=100, blank=True, null=True)
    # zoom_join_url = models.URLField(blank=True, null=True)
    # zoom_start_url = models.URLField(blank=True, null=True)
    zoom_meeting_id = models.CharField(max_length=100, blank=True, null=True)

    zoom_join_url = models.TextField(blank=True, null=True)
    zoom_start_url = models.TextField(blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.user.username} with {self.doctor.user.username} on {self.date}"


# -------------------- HEALTH DATA --------------------
class HealthData(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    blood_pressure = models.CharField(max_length=20, blank=True)
    sugar = models.CharField(max_length=20, blank=True)
    pse = models.CharField(max_length=20, blank=True)  # Pulse/SpO2/ECG
    weight = models.CharField(max_length=20, blank=True)
    notes = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.patient.user.username} - {self.date}"

# -------------------- PAYMENT --------------------
class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='payments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Payment {self.id} - {self.patient.user.username} to {self.doctor.user.username}"


# -------------------- PRESCRIPTION --------------------
class Prescription(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    diagnosis = models.TextField()
    medicines = models.TextField()
    doctor_notes = models.TextField(blank=True)

    report_file = models.FileField(upload_to='prescriptions/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription - {self.patient.user.username}"


# -------------------- health alert --------------------
class HealthAlert(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    health_data = models.ForeignKey(HealthData, on_delete=models.CASCADE)
    parameter = models.CharField(max_length=50)  # sugar / bp / pulse
    value = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Alert - {self.patient.user.username}"
