
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PatientRecordForm, PrescriptionForm
from admins.models import Patient, PatientRecord, Appointment, LoginTable




def manage_patient_records(request):
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
            return redirect('manage_patient_records')
    else:
        form = PatientRecordForm()

    return render(request, 'doctor/manage_records.html', {'form': form, 'patients': patients, 'records': records, 'query': query})


def update_patient_record(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)

    if request.method == 'POST':
        form = PatientRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('manage_patient_records')  # Redirect to the manage records page or another relevant page
    else:
        form = PatientRecordForm(instance=record)

    return render(request, 'doctor/update_record.html', {'form': form})






# @login_required
def view_patient_record(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)
    return render(request, 'doctor/view_record.html', {'record': record})


# @login_required
def delete_patient_record(request, record_id):
    record = get_object_or_404(PatientRecord, id=record_id)
    patient_id = record.patient.id
    if request.method == 'POST':
        record.delete()
        return redirect('manage_patient_records')
    return render(request, 'doctor/confirm_delete.html', {'record': record})


# @login_required
def e_prescribe(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.save()
            return redirect('e_prescribe')
    else:
        form = PrescriptionForm()
        form.fields['doctor'].queryset = LoginTable.objects.filter(type='doctor')
        form.fields['patient'].queryset = Patient.objects.filter(type='patient')
    return render(request, 'doctor/e_prescribe.html', {'form': form})



