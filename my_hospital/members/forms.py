from django import forms
from django.contrib.auth.models import User
from .models import Patient, Doctor, HealthData, Appointment, Payment





class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'phone', 'assigned_doctor','user']


class AdminPatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['age', 'phone', 'assigned_doctor','user']



# class DoctorRegisterForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = ['specialization', 'phone', 'fee']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
       
#         self.fields['specialization'].required = True

from django import forms
from django.contrib.auth.models import User
from .models import Doctor

class DoctorRegisterForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'})
    )

    class Meta:
        model = Doctor
        fields = ['specialization', 'phone', 'fee']  # keep old fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialization'].required = True

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class HealthForm(forms.ModelForm):
    class Meta:
        model = HealthData
        fields = ['blood_pressure', 'sugar', 'pse', 'weight', 'notes']



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['transaction_id']


class PaymentGatewayForm(forms.Form):
    cardholder_name = forms.CharField(label='Name on Card', max_length=100, required=True,
                                      widget=forms.TextInput(attrs={'class':'form-control', 'id':'id_cardholder_name'}))
    card_number = forms.CharField(label='Card Number', max_length=19, required=True,
                                  widget=forms.TextInput(attrs={'class':'form-control', 'id':'id_card_number', 'placeholder':'1234 5678 9012 3456'}))
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=[(str(i), f"{i:02}") for i in range(1,13)],
                                     widget=forms.Select(attrs={'class':'form-select me-2', 'id':'id_expiry_month'}))
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=[(str(y), str(y)) for y in range(2025, 2035)],
                                    widget=forms.Select(attrs={'class':'form-select', 'id':'id_expiry_year'}))
    cvv = forms.CharField(label='CVV', max_length=4, required=True,
                          widget=forms.PasswordInput(render_value=False, attrs={'class':'form-control', 'id':'id_cvv', 'placeholder':'123'}))

    def clean_card_number(self):
        data = self.cleaned_data['card_number'].replace(' ', '')
        if not data.isdigit() or not (13 <= len(data) <= 19):
            raise forms.ValidationError('Enter a valid card number')
        return data

    def clean_cvv(self):
        data = self.cleaned_data['cvv']
        if not data.isdigit() or len(data) not in (3, 4):
            raise forms.ValidationError('Enter a valid CVV')
        return data


class PinForm(forms.Form):
    pin = forms.CharField(label='Enter PIN', max_length=6, required=True,
                          widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter 4-digit PIN'}))

    def clean_pin(self):
        data = self.cleaned_data['pin']
        if not data.isdigit() or len(data) not in (3, 4, 6):
            raise forms.ValidationError('PIN must be numeric and 3, 4 or 6 digits long')
        return data

