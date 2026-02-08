

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import HealthData, HealthAlert


@receiver(post_save, sender=HealthData)
def generate_health_alert(sender, instance, created, **kwargs):
    patient = instance.patient
    doctor = patient.assigned_doctor
    thresholds = settings.HEALTH_THRESHOLDS

    # ---------- Sugar ----------
    if instance.sugar:
        sugar = float(instance.sugar)
        low, high = thresholds['sugar']
        if sugar < low or sugar > high:
            HealthAlert.objects.create(
                patient=patient,
                doctor=doctor,
                health_data=instance,
                parameter='Sugar',
                value=instance.sugar,
                message=f'Sugar level abnormal ({low}-{high} mg/dL)'
            )

    # ---------- Weight ----------
    if instance.weight:
        weight = float(instance.weight)
        low, high = thresholds['weight']
        if weight < low or weight > high:
            HealthAlert.objects.create(
                patient=patient,
                doctor=doctor,
                health_data=instance,
                parameter='Weight',
                value=instance.weight,
                message=f'Weight out of range ({low}-{high} kg)'
            )

    # ---------- Blood Pressure ----------
    if instance.blood_pressure:
        try:
            systolic, diastolic = map(int, instance.blood_pressure.split('/'))

            sys_low, sys_high = thresholds['blood_pressure_systolic']
            dia_low, dia_high = thresholds['blood_pressure_diastolic']

            if systolic < sys_low or systolic > sys_high:
                HealthAlert.objects.create(
                    patient=patient,
                    doctor=doctor,
                    health_data=instance,
                    parameter='Systolic BP',
                    value=str(systolic),
                    message='Systolic BP abnormal'
                )

            if diastolic < dia_low or diastolic > dia_high:
                HealthAlert.objects.create(
                    patient=patient,
                    doctor=doctor,
                    health_data=instance,
                    parameter='Diastolic BP',
                    value=str(diastolic),
                    message='Diastolic BP abnormal'
                )
        except:
            pass

    # ---------- Pulse & SpO2 ----------
    if instance.pse:
        try:
            pulse, spo2 = map(int, instance.pse.split('/'))

            p_low, p_high = thresholds['pulse']
            s_low, s_high = thresholds['spo2']

            if pulse < p_low or pulse > p_high:
                HealthAlert.objects.create(
                    patient=patient,
                    doctor=doctor,
                    health_data=instance,
                    parameter='Pulse',
                    value=str(pulse),
                    message='Pulse rate abnormal'
                )

            if spo2 < s_low:
                HealthAlert.objects.create(
                    patient=patient,
                    doctor=doctor,
                    health_data=instance,
                    parameter='SpO2',
                    value=str(spo2),
                    message='Low oxygen saturation'
                )
        except:
            pass
