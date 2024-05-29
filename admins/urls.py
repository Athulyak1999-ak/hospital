from django.urls import path
from .views import manage_users, create_billing, manage_facilities, admin_create_appointment, admin_update_appointment, admin_delete_appointment, admin_appointment_list, update_billing, delete_billing, update_user, delete_user, admin_manage_patient_records, admin_update_patient_record, admin_delete_patient_record

urlpatterns = [
    path('manage_users/', manage_users, name='manage_users'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('manage_facilities/', manage_facilities, name='manage_facilities'),
    path('admin_appointments_new/', admin_create_appointment, name='admin_create_appointment'),
    path('admin_appointments/update/<int:pk>/', admin_update_appointment, name='admin_update_appointment'),
    path('admin_appointments/delete/<int:pk>/', admin_delete_appointment, name='admin_delete_appointment'),
    path('admin_appointments/', admin_appointment_list, name='admin_appointment_list'),
    path('billing_create/', create_billing, name='create_billing'),
    path('update_billing/<int:pk>/', update_billing, name='update_billing'),
    path('delete_billing/<int:billing_id>/', delete_billing, name='admin_delete_billing'),
    path('admin_patients_records/', admin_manage_patient_records, name='admin_manage_patient_records'),
    path('delete_records/<int:record_id>/', admin_delete_patient_record, name='admin_delete_record'),
    path('admin_record_update/<int:record_id>/', admin_update_patient_record, name='admin_update_patient_record'),
]
