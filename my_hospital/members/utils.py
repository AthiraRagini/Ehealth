from django.conf import settings
from .models import HealthAlert


def generate_health_alerts(patient, doctor, health_data):
    thresholds = settings.HEALTH_THRESHOLDS
    alerts = []

    # Blood Pressure
    if health_data.blood_pressure:
        try:
            sys, dia = map(int, health_data.blood_pressure.split('/'))

            if not (thresholds['blood_pressure_systolic'][0] <= sys <= thresholds['blood_pressure_systolic'][1]):
                alerts.append({
                    'parameter': 'blood_pressure_systolic',
                    'value': sys,
                    'message': f"Systolic BP out of range: {sys} mmHg"
                })

            if not (thresholds['blood_pressure_diastolic'][0] <= dia <= thresholds['blood_pressure_diastolic'][1]):
                alerts.append({
                    'parameter': 'blood_pressure_diastolic',
                    'value': dia,
                    'message': f"Diastolic BP out of range: {dia} mmHg"
                })

        except ValueError:
            alerts.append({
                'parameter': 'blood_pressure',
                'value': health_data.blood_pressure,
                'message': 'Invalid blood pressure format'
            })

    # Sugar
    if health_data.sugar:
        sugar = int(health_data.sugar)
        if not (thresholds['sugar'][0] <= sugar <= thresholds['sugar'][1]):
            alerts.append({
                'parameter': 'sugar',
                'value': sugar,
                'message': f"Sugar level abnormal: {sugar} mg/dL"
            })

    # PSE
    if health_data.pse:
        pse = float(health_data.pse)
        if pse > thresholds.get('pse_max', 4):
            alerts.append({
                'parameter': 'pse',
                'value': pse,
                'message': f"PSE value abnormal: {pse}"
            })

    # Weight
    if health_data.weight:
        weight = float(health_data.weight)
        if not (thresholds['weight'][0] <= weight <= thresholds['weight'][1]):
            alerts.append({
                'parameter': 'weight',
                'value': weight,
                'message': f"Weight out of range: {weight} kg"
            })

    # Save alerts
    for alert in alerts:
        HealthAlert.objects.create(
            patient=patient,
            doctor=doctor,
            health_data=health_data,
            parameter=alert['parameter'],
            value=str(alert['value']),
            message=alert['message']
        )
