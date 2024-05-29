from django.db import models


class Patient(models.Model):
    username = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=200)
    con_password = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medical_history = models.TextField()
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()

    def __str__(self):
        return f'Medical Record for {self.patient.username}'


class LoginTable(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
    type = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.username)


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Rescheduled', 'Rescheduled'), ('Cancelled', 'Cancelled')])
    def __str__(self):
        return f"{self.patient.username} - {self.date} with {self.doctor.username}"



class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    instructions = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.username} by {self.doctor.username} on {self.date}"


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    insurance_info = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.patient.username} - {self.amount} on {self.date}"


class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    departments = models.CharField(max_length=255)
    resources = models.TextField()

    def __str__(self):
        return self.name


# class PatientRecord(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_records')
#     diagnosis = models.TextField()
#     treatment_plan = models.TextField()
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.patient.username} - {self.doctor} on {self.date}"
#
#


#
#
# class Facility(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     departments = models.CharField(max_length=255)
#     resources = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
# class AdminAppointment(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
#     date = models.DateTimeField()
#     status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Rescheduled', 'Rescheduled'), ('Cancelled', 'Cancelled')])
#
#     def __str__(self):
#         return f"Appointment on {self.date} with {self.doctor.username}"
#
#
#
# class PatientRecord(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='records')
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_records')
#     diagnosis = models.TextField()
#     treatment_plan = models.TextField()
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.patient.username} - {self.doctor} on {self.date}"
#
#
# class Prescription(models.Model):
#     patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
#     doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_prescriptions')
#     medication = models.CharField(max_length=255)
#     dosage = models.CharField(max_length=255)
#     instructions = models.TextField()
#     date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Prescription for {self.patient.username} by {self.doctor.username} on {self.date}"
#
#
#
# class UserProfile(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     password2 = models.CharField(max_length=300)
#
#     def __str__(self):
#         return '{}'.format(self.username)
#
# class LoginTable(models.Model):
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     password2 = models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#
#     def __str__(self):
#         return '{}'.format(self.username)
#
#
# class Patient(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     address = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     medical_history = models.TextField()
#
#     def __str__(self):
#         return self.user.username
#
#
# class Appointment(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     doctor = models.CharField(max_length=255)
#     status = models.CharField(max_length=20, choices=[('Scheduled', 'Scheduled'), ('Rescheduled', 'Rescheduled'), ('Cancelled', 'Cancelled')])
#     def __str__(self):
#         return f"{self.patient.user.username} - {self.date} with {self.doctor}"
#
# class MedicalHistory(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     record_date = models.DateField()
#     diagnosis = models.CharField(max_length=255)
#     treatment = models.TextField()
#
#     def __str__(self):
#         return f"{self.patient.user.username} - {self.diagnosis}"
#
#
# class Billing(models.Model):
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     date = models.DateField()
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     paid = models.BooleanField(default=False)
#     insurance_info = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         return f"{self.patient.user.username} - {self.amount} on {self.date}"
