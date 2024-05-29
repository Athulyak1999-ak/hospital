from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.userRegistration, name='register'),
    path('patient_view/', views.patient_view, name='patient_view'),
    path('doctor_login/', views.UserLoginPage, name='doctor_login'),
    path('doctor_register/', views.DoctorRegistration, name='doctor_register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('doctor_view/', views.doctor_view, name='doctor_view'),
    path('user_logout/', views.user_logout_view, name='user_logout'),
    path('doctor_logout/', views.doctor_logout_view, name='doctor_logout')

]
