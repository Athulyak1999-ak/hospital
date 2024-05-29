# patients/urls.py

from django.urls import path
from . import views
# from .views import index, patient_home, register, book_appointment, view_appointments, view_medical_history, view_billing, health_education

urlpatterns = [
    # path('register/', register, name='register'),
    # path('book_appointment/', book_appointment, name='book_appointment'),
    # path('appointments/', view_appointments, name='appointment_list'),
    # path('medical_history/', view_medical_history, name='medical_history'),
    # path('billing/', view_billing, name='billing'),
    # path('health_education/', health_education, name='health_education'),
    # path('index/', index, name='index'),
    # path('patient_home/', patient_home, name='patient_home'),
    path('appointments_new/', views.create_appointment, name='create_appointment'),
    path('appointments/update/<int:pk>/', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('billing/', views.view_billing, name='billing'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
# error sloved last
    path('medical_history/<int:record_id>/', views.view_medical_record, name='medical_history'),

]
