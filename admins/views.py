from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm, CreateBillingForm, FacilityForm
from doctors.forms import PatientRecordForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import LoginTable, Patient, Billing, Facility,Appointment,PatientRecord
from patients.forms import AppointmentForm
from django.db.models import Q
from django.contrib import messages



def admin_required(view_func):
    return user_passes_test(lambda u: u.is_staff, login_url='/admin/login/')(view_func)

# @admin_required
def manage_users(request):
    users_list = LoginTable.objects.filter(type='doctor')

    query = request.GET.get('q')
    if query:
        users_list = users_list.filter(username__icontains=query)

    paginator = Paginator(users_list, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm()

    return render(request, 'admin/manage_users.html', {'users': users, 'form': form})


def update_user(request, user_id):
    user_instance = get_object_or_404(LoginTable, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            return redirect('manage_users')
    else:
        form = UserForm(instance=user_instance)
    return render(request, 'admin/update_user.html', {'form': form, 'user_instance': user_instance})


def delete_user(request, user_id):
    user = get_object_or_404(LoginTable, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('manage_users')
    return render(request, 'admin/confirm_delete.html', {'user': user})


def admin_create_appointment(request):
    query = request.GET.get('q')
    if query:
        appointments_list = Appointment.objects.filter(
            Q(patient__username__icontains=query) |
            Q(doctor__username__icontains=query) |
            Q(date__icontains=query) |
            Q(status__icontains=query)
        )
    else:
        appointments_list = Appointment.objects.all()

    paginator = Paginator(appointments_list, 10)  # Show 10 appointments per page.
    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_create_appointment')  # Redirect to a success page or reload.
    else:
        form = AppointmentForm()
        form.fields['doctor'].queryset = LoginTable.objects.filter(type='doctor')

    return render(request, 'admin/create_appointment.html', {'form': form, 'appointments': appointments, 'query': query})

# @login_required
def admin_update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('admin_create_appointment')  # Ensure this view exists
    else:
        form = AppointmentForm(instance=appointment)
        form.fields['doctor'].queryset = LoginTable.objects.filter(type='doctor')
    return render(request, 'patients/update_appointment.html', {'form': form, 'appointment': appointment})

# @login_required
def admin_delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('admin_create_appointment')  # Ensure this view exists
    return render(request, 'patients/delete_appointment.html', {'appointment': appointment})


# @login_required
def admin_appointment_list(request):
    query = request.GET.get('q', '')
    appointment_list = Appointment.objects.filter(
        patient__username__icontains=query) if query else Appointment.objects.all()

    paginator = Paginator(appointment_list, 5)  # Show 10 appointments per page.
    page_number = request.GET.get('page')
    appointments = paginator.get_page(page_number)

    return render(request, 'admin/appointment_list.html', {'appointments': appointments, 'query': query})


# @login_required
def create_billing(request):
    query = request.GET.get('q')
    bills = Billing.objects.all()
    if query:
        bills = bills.filter(patient__username__icontains=query)  # Adjust field based on your model's search criteria

    paginator = Paginator(bills, 5)  # Show 10 bills per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = CreateBillingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreateBillingForm()
        form.fields['patient'].queryset = Patient.objects.filter(type='patient')

    return render(request, 'admin/create_billing.html', {'form': form, 'page_obj': page_obj, 'query': query})

def update_billing(request, pk):
    billing_record = get_object_or_404(Billing, pk=pk)
    if request.method == 'POST':
        form = CreateBillingForm(request.POST, instance=billing_record)
        if form.is_valid():
            form.save()
            return redirect('create_billing')  # Redirect to billing records page or any other page
    else:
        form = CreateBillingForm(instance=billing_record)
    return render(request, 'admin/update_billing.html', {'form': form, 'billing_record': billing_record})


def delete_billing(request, billing_id):
    billing_record = get_object_or_404(Billing, id=billing_id)
    if request.method == 'POST':
        billing_record.delete()
        messages.success(request, 'Billing record deleted successfully.')
        return redirect('create_billing')  # Adjust this redirect to your billing list view
    return render(request, 'admin/delete_billing.html', {'billing': billing_record})

# @admin_required
def manage_facilities(request):
    facilities = Facility.objects.all()
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_facilities')
    else:
        form = FacilityForm()
    return render(request, 'admin/manage_facilities.html', {'facilities': facilities, 'form': form})


def admin_manage_patient_records(request):
    # Fetch all patients with type 'patient'
    patients = Patient.objects.filter(type='patient')

    # Get the search query if it exists
    query = request.GET.get('q')
    if query:
        records = PatientRecord.objects.filter(patient__username__icontains=query, patient__in=patients)
    else:
        records = PatientRecord.objects.filter(patient__in=patients)

    # Pagination setup
    paginator = Paginator(records, 5)  # Show 5 records per page
    page = request.GET.get('page')

    try:
        records = paginator.page(page)
    except PageNotAnInteger:
        records = paginator.page(1)
    except EmptyPage:
        records = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = PatientRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_patient_records')
    else:
        form = PatientRecordForm()

    return render(request, 'admin/admin_manage_patients_records.html', {'form': form, 'patients': patients, 'records': records, 'query': query})


def admin_update_patient_record(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)

    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('admin_manage_patient_records')  # Redirect to the manage records page or another relevant page
    else:
        form = PatientRecordForm(instance=record)

    return render(request, 'admin/admin_update_patient_record.html', {'form': form})

#
# # @login_required
def admin_delete_patient_record(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)
    patient_id = record.patient.id

    if request.method == 'POST':
        record.delete()
        return redirect('admin_manage_patient_records')

    return render(request, 'admin/admin_patient_record_confirm_delete.html', {'record': record})
