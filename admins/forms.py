from django import forms
from django.contrib.auth.models import User
# from .models import Facility, AdminAppointment
from .models import LoginTable, Billing, Facility

class UserForm(forms.ModelForm):
    class Meta:
        model = LoginTable
        fields = '__all__'


class CreateBillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'date', 'amount', 'paid', 'insurance_info']
        widgets = {
            'patient': forms.Select(),
            'date': forms.SelectDateWidget(),
            'amount': forms.NumberInput(attrs={'step': 0.01}),
            'paid': forms.CheckboxInput(),
            'insurance_info': forms.TextInput(attrs={'placeholder': 'Enter insurance information'}),
        }

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'departments', 'resources']
