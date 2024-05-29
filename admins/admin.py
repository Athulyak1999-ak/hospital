# patients/admin.py
from django.contrib import admin
from .models import Patient, PatientRecord, LoginTable, Appointment, Prescription, Billing

admin.site.register(Patient)
admin.site.register(PatientRecord)
admin.site.register(LoginTable)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Billing)
