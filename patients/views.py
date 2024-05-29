# # patients/views.py
#
# from django.shortcuts import render, redirect
# from .forms import PatientRegistrationForm, AppointmentForm, BillingForm, MedicalHistoryForm
# from .models import Patient, Appointment, Billing, MedicalHistory
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from admins.models import LoginTable, Appointment, PatientRecord, Patient, Billing
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import stripe



# @login_required
def create_appointment(request):
    if 'id' in request.session:
        patient_id = request.session['id']
        patient = Patient.objects.get(id=patient_id)
        appointment_records = Appointment.objects.filter(patient=patient)

        # Pagination
        paginator = Paginator(appointment_records, 5)  # Show 10 appointments per page
        page = request.GET.get('page')
        try:
            appointments = paginator.page(page)
        except PageNotAnInteger:
            appointments = paginator.page(1)
        except EmptyPage:
            appointments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AppointmentForm()
        form.fields['doctor'].queryset = LoginTable.objects.filter(type='doctor')

    return render(request, 'patients/create_appointment.html', {'form': form, 'appointments': appointments})


# @login_required
def update_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('create_appointment')  # Ensure this view exists
    else:
        form = AppointmentForm(instance=appointment)
        form.fields['doctor'].queryset = LoginTable.objects.filter(type='doctor')
    return render(request, 'patients/update_appointment.html', {'form': form, 'appointment': appointment})

# @login_required
def delete_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('create_appointment')  # Ensure this view exists
    return render(request, 'patients/delete_appointment.html', {'appointment': appointment})


# @login_required
def view_medical_record(request, record_id):
    patient = get_object_or_404(Patient, id=record_id)
    records = PatientRecord.objects.filter(patient=patient)
    return render(request, 'patients/patient_medical_records.html', {'patient': patient, 'records': records})

# @login_required
def view_billing(request):
    if 'id' in request.session:
        patient_id = request.session['id']
        patient = Patient.objects.get(id=patient_id)
        bills = Billing.objects.filter(patient=patient)
        # total_amount = sum(bill.amount for bill in bills)
        return render(request, 'patients/billing.html', {'bills': bills, 'patient': patient})


def create_checkout_session(request):
    if 'id' in request.session:
        patient_id = request.session['id']
        patient = Patient.objects.get(id=patient_id)
        bills = Billing.objects.filter(patient=patient)
        if bills:
            stripe.api_key = settings.STRIPE_SECRET_KEY

            if request.method == 'POST':
                line_items = []
                for bill in bills:
                        line_item = {
                            'price_data': {
                                'currency': 'INR',
                                'unit_amount': int(bill.amount * 100),  # Amount in cents
                                'product_data': {
                                    'name': f'Billing Statement {bill.date}'
                                },
                            },
                            'quantity': 1,
                        }
                        line_items.append(line_item)
            if line_items:
                checkout_session = stripe.checkout.Session.create (
                    payment_method_types=['card'],
                    line_items=line_items,
                    mode='payment',
                    success_url=request.build_absolute_uri(reverse('success')),
                    cancel_url=request.build_absolute_uri(reverse('cancel'))

                )
                return redirect(checkout_session.url, code=303)
    return redirect('billing')


def success(request):
    if 'id' in request.session:
        patient_id = request.session['id']
        patient = Patient.objects.get(id=patient_id)
        bills = Billing.objects.filter(patient=patient)
        for bill in bills:
            bill.paid = True
            bill.amount = 0
            bill.save()
        return render(request, 'patients/success.html')


def cancel(request):
    return render(request, 'patients/cancel.html')

##     if cart_items:
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#
#         if request.method == 'POST':
#             line_items = []
#             for cart_item in cart_items:
#                 if cart_item.book:
#                     line_item ={
#                         'price_data': {
#                             'currency': 'INR',
#                             'unit_amount':int(cart_item.book.price*100),
#                             'product_data':{
#                                 'name': cart_item.book.title
#                             },
#                         },
#                         'quantity': 1   #cart_item.book.quantity
#                     }
#                     line_items.append(line_item)
#             if line_items:
#                 checkout_session = stripe.checkout.Session.create (
#                     payment_method_types=['card'],
#                     line_items=line_items,
#                     mode='payment',
#                     success_url=request.build_absolute_uri(reverse('success')),
#                     cancel_url=request.build_absolute_uri(reverse('cancel'))
#
#                 )
#                 return redirect(checkout_session.url,code=303)
#


#
# def medical_history(request, record_id):
#     patient = get_object_or_404(Patient, id=record_id)
#     medical_history_records = PatientRecord.objects.filter(patient=patient)
#     return render(request, 'patients/medical_history.html', {
#         'patient': patient,
#         'medical_history_records': medical_history_records
#     })
#
# @login_required
# def view_medical_history(request):
#     medical_histories = MHistory.objects.filter(patient=request.patient)
#     return render(request, 'patients/medical_history.html', {'medical_histories': medical_histories})
#



# def register(request):
#     if request.method == 'POST':
#         form = PatientRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = PatientRegistrationForm()
#     return render(request, 'patients/register.html', {'form': form})
#
# @login_required
# def book_appointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.patient = request.user.patient
#             appointment.save()
#             return redirect('appointment_list')
#     else:
#         form = AppointmentForm()
#     return render(request, 'patients/book_appointment.html', {'form': form})
#
# @login_required
# def view_appointments(request):
#     appointments = Appointment.objects.filter(patient=request.user.patient)
#     return render(request, 'patients/appointments.html', {'appointments': appointments})
#
# @login_required
# def view_medical_history(request):
#     medical_histories = MedicalHistory.objects.filter(patient=request.user.patient)
#     return render(request, 'patients/medical_history.html', {'medical_histories': medical_histories})
#
# @login_required
# def view_billing(request):
#     bills = Billing.objects.filter(patient=request.user.patient)
#     return render(request, 'patients/billing.html', {'bills': bills})
#
# @login_required
# def health_education(request):
#     return render(request, 'patients/health_education.html')
#
# def index(request):
#     return render(request, 'index.html')
#
#
# def patient_home(request):
#     return render(request, 'patients/patient_home.html')
