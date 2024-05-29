from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import UserProfile, LoginTable
# # from .forms import PatientRegistrationForm
# from patients.models import Patient
from .forms import UserProfileForm, LoginTableForm
from admins.models import Patient, LoginTable, PatientRecord

# Create your views here.


def userRegistration(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            login_record = form.save(commit=False)
            login_record.type = 'patient'
            login_record.save()
            messages.info(request, 'Registration success')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please check your inputs.')
    else:
        form = UserProfileForm()
    return render(request, 'login/patient_register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Patient.objects.filter(username=username, password=password, type='patient').exists()
        try:

            if user is not None:
                user_details = Patient.objects.get(username=username, password=password)
                user_name = user_details.username
                patient_id = user_details.id
                type = user_details.type
                if type == 'patient':
                    request.session['username'] = user_name
                    request.session['id'] = patient_id
                    return redirect('patient_view')
            else:
                messages.error(request, 'Invalid username or password')
        except:
            messages.error(request, 'invalid role')
    return render(request, 'login/admin_login.html')


def DoctorRegistration(request):
    if request.method == 'POST':
        form = LoginTableForm(request.POST)
        if form.is_valid():
            login_record = form.save(commit=False)
            login_record.type = 'doctor'
            login_record.save()
            messages.info(request, 'Registration success')
            return redirect('doctor_login')
        else:
            messages.error(request, 'Registration failed. Please check your inputs.')
    else:
        form = LoginTableForm()
    return render(request, 'login/doctor_register.html', {'form': form})



def UserLoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = LoginTable.objects.filter(username=username, password=password, type='doctor').exists()
        try:

            if user is not None:
                user_details = LoginTable.objects.get(username=username, password=password)
                user_name = user_details.username
                type = user_details.type
                if type == 'doctor':
                    request.session['username'] = user_name
                    return redirect('doctor_view')
                elif type == 'admin':
                    request.session['username'] = user_name
                    return redirect('admin_view')
            else:
                messages.error(request, 'Invalid username or password')
        except:
            messages.error(request, 'invalid role')
    return render(request, 'login/doctor_login.html')


def patient_view(request):
    if 'id' in request.session:
        patient_id = request.session['id']
        patient = Patient.objects.get(id=patient_id)
        patient_records = PatientRecord.objects.filter(patient=patient)
        return render(request, 'patients/patient_home.html', {'patient': patient, 'patient_records': patient_records})
    else:
        return redirect('login')
    # user_name = request.session['username']
    # return render(request, 'patients/patient_home.html', {'user_name': user_name})

def admin_view(request):
    user_name = request.session['username']
    return render(request, 'admin/admin_home.html', {'user_name': user_name})


def doctor_view(request):
    user_name = request.session['username']
    return render(request, 'doctor/doctor_home.html', {'user_name': user_name})

def user_logout_view(request):
    logout(request)
    return redirect('login')


def doctor_logout_view(request):
    logout(request)
    return redirect('doctor_login')


def homepage(request):
    return render(request, 'index.html')



   # if request.method == 'POST':
   #     form = UserProfileForm(request.POST)
   #     if form.is_valid():
   #       login_record = form.save(commit=False)
   #       login_record.type = 'patient'
   #       login_record.save()
   #       messages.info(request, 'Registration success')
   #       return redirect('login')
   #     else:
   #         messages.error(request, 'Registration failed. Please check your inputs.')
   # else:
   #     form = UserProfileForm()
   #
   # return render(request, 'login/patient_register.html', {'form': form})


# def userRegistration(request):
#   # login_table = LoginTable()
#     # userprofile = UserProfile()
#     # if request.method == 'POST':
#     #     userprofile.username = request.POST['username']
#     #     userprofile.password = request.POST['password']
#     #     userprofile.password2 = request.POST['password1']
#     #
#     #     login_table.username = request.POST['username']
#     #     login_table.password = request.POST['password']
#     #     login_table.password2 = request.POST['password1']
#     #     login_table.type = 'patient'
#     #
#     #     if request.POST['password'] == request.POST['password']:
#     #         userprofile.save()
#     #         login_table.save()
#     #         messages.info(request, 'Registration success')
#     #         return redirect('login')
#     #     else:
#     #         messages.info(request, 'Password not matching')
#     #         return redirect('register')
#     #
#     # return render(request, 'login/patient_register.html')
#     if request.method == 'POST':
#         form = LoginTableForm(request.POST)
#         form1 = UserProfileForm(request.POST)
#         if form.is_valid() and form1.is_valid():
#             form1.save()
#             login_record = form.save(commit=False)
#             login_record.type = 'patient'
#             login_record.save()
#             messages.info(request, 'Registration success')
#             return redirect('login')
#         else:
#             messages.error(request, 'Registration failed. Please check your inputs.')
#     else:
#         form = UserProfileForm()
#     return render(request, 'login/patient_register.html', {'form': form})
#
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = LoginTable.objects.filter(username=username, password=password, type='patient').exists()
#         try:
#
#             if user is not None:
#                 user_details = LoginTable.objects.get(username=username, password=password)
#                 user_name = user_details.username
#                 type = user_details.type
#                 if type == 'doctor':
#                     request.session['username'] = user_name
#                     return redirect('user_view')
#                 elif type == 'admin':
#                     request.session['username'] = user_name
#                     return redirect('admin_view')
#                 elif type == 'patient':
#                     request.session['username'] = user_name
#                     return redirect('patient_view')
#             else:
#                 messages.error(request, 'Invalid username or password')
#         except:
#             messages.error(request, 'invalid role')
#     return render(request, 'login/admin_login.html')
#
#
# def admin_view(request):
#     user_name = request.session['username']
#     return render(request, 'admin/admin_home.html', {'user_name': user_name})
#     # return redirect('admin_home')
#
# def user_view(request):
#     user_name = request.session['username']
# # return render(request, 'user/user_listBook.html', {'user_name': user_name})
#     return redirect('doctor_home')
#
#
# def patient_view(request):
#     user_name = request.session['username']
#     return render(request, 'patients/patient_home.html', {'user_name': user_name})
#     # return redirect('admin_home')
#
#
# #
# #
# # def register(request):
# #     if request.method == 'POST':
# #         form = PatientRegistrationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('login')
# #     else:
# #         form = PatientRegistrationForm()
# #     return render(request, 'patients/register.html', {'form': form})
# #
# # #
# def logout_view(request):
#     logout(request)
#     return redirect('login')
#
#
#
#
