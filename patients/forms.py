# patients/forms.py

from django import forms
from admins.models import Appointment


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'doctor', 'patient', 'status']  # Ensure 'patient' field is included in the fields list

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'doctor': forms.Select(),
            'patient': forms.Select(),
            'status': forms.Select(choices=[('Scheduled', 'Scheduled'), ('Rescheduled', 'Rescheduled'), ('Cancelled', 'Cancelled')]),
        }

        labels = {
            'date': 'Appointment Date',
            'doctor': 'Doctor',
            'patient': 'Patient',
            'status': 'Status',
        }

#
# class BillingRecord(forms.ModelForm):
#     class Meta:
#         model = TotalBillAmount
#         fields = ['patient', 'total_amount']

# class PatientRegistrationForm(forms.ModelForm):
#     username = forms.CharField(max_length=30)
#     password = forms.CharField(widget=forms.PasswordInput)
#     date_of_birth = forms.DateField(widget=forms.SelectDateWidget)
#
#     class Meta:
#         model = Patient
#         fields = ['username', 'password', 'date_of_birth', 'address', 'phone_number']
#
#     def save(self, commit=True):
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             password=self.cleaned_data['password']
#         )
#         patient = Patient(
#             user=user,
#             date_of_birth=self.cleaned_data['date_of_birth'],
#             address=self.cleaned_data['address'],
#             phone_number=self.cleaned_data['phone_number']
#         )
#         if commit:
#             patient.save()
#         return patient
#
#
# class AppointmentForm(forms.ModelForm):
#     class Meta:
#         model = Appointment
#         fields = ['date', 'doctor']
#
#
# class BillingForm(forms.ModelForm):
#     class Meta:
#         model = Billing
#         fields = ['amount', 'insurance_info']
#
#
# class MedicalHistoryForm(forms.ModelForm):
#     class Meta:
#         model = MedicalHistory
#         fields = ['record_date', 'diagnosis', 'treatment']
#
#
