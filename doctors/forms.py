from django import forms
from admins.models import PatientRecord, Prescription

class PatientRecordForm(forms.ModelForm):
    class Meta:
        model = PatientRecord
        fields = ['patient', 'medical_history', 'diagnosis', 'medications', 'allergies', 'treatment_history']

        widgets = {
            'patient': forms.Select(),
            'medical_history': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'diagnosis': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'medications': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'allergies': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'treatment_history': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

        labels = {
            'patient': 'Patient',
            'medical_history': 'Medical History',
            'diagnosis': 'Diagnosis',
            'medications': 'Medications',
            'allergies': 'Allergies',
            'treatment_history': 'Treatment History',
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'medication', 'dosage', 'instructions']
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'medication': forms.TextInput(attrs={'class': 'form-control'}),
            'dosage': forms.TextInput(attrs={'class': 'form-control'}),
            'instructions': forms.Textarea(attrs={'class': 'form-control'}),
        }


