from datetime import timedelta
from django.shortcuts import render, redirect
from .forms import PatientSignUpForm
from clinics.models import Appointment
from django.utils import timezone
from clinics.models import Review

def register_patient(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_patient = True
            user.save()
            # Logowanie użytkownika po rejestracji i przekierowanie do strony profilu
            # return redirect('index')  # Zakładamy, że 'index' to strona główna
    else:
        form = PatientSignUpForm()
    return render(request, 'patients/register.html', {'form': form})

def book_appointment(request, specialist_id):
    if request.method == 'POST':
        date_time = request.POST.get('date_time')
        Appointment.objects.create(patient=request.user.patient, specialist_id=specialist_id, date_time=date_time, status='Scheduled')
        return redirect('appointments_list')
    return render(request, 'patients/book_appointment.html')

def appointments_list(request):
    appointments = Appointment.objects.filter(patient=request.user.patient, date_time__gte=timezone.now()).order_by('date_time')
    return render(request, 'patients/appointments_list.html', {'appointments': appointments})

def cancel_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    # Sprawdź, czy anulowanie jest możliwe (24h przed wizytą)
    if appointment.date_time - timezone.now() > timedelta(hours=24):
        appointment.status = 'Cancelled'
        appointment.save()
    return redirect('appointments_list')


def add_review(request, specialist_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment', '')
        Review.objects.create(patient=request.user.patient, specialist_id=specialist_id, rating=rating, comment=comment)
        return redirect('specialist_detail', specialist_id=specialist_id)
    return render(request, 'patients/add_review.html')
