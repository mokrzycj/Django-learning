from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment, Review
# from .forms import ReviewForm
from .models import Availability
from .forms import AvailabilityForm
from django.contrib.auth.decorators import login_required
from .models import Availability, Profile
from datetime import datetime

def book_appointment(request, specialist_id):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.profile
            appointment.specialist_id = specialist_id
            appointment.save()
            messages.success(request, 'Wizyta została pomyślnie zarezerwowana!')
            return redirect('dashboard_patient')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def patient_appointments(request):
    appointments = Appointment.objects.filter(patient=request.user.profile).order_by('date', 'time')
    return render(request, 'patient_appointments.html', {'appointments': appointments})

def specialist_appointments(request):
    appointments = Appointment.objects.filter(specialist=request.user.profile).order_by('date', 'time')
    return render(request, 'specialist_appointments.html', {'appointments': appointments})

def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Wizyta została pomyślnie anulowana.')
        return redirect('dashboard_patient')
    return render(request, 'cancel_appointment.html', {'appointment': appointment})

def confirm_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    appointment.status = 'confirmed'
    appointment.save()
    messages.success(request, 'Wizyta została pomyślnie potwierdzona.')
    return redirect('dashboard_specialist')

def add_review(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.appointment = appointment
            review.patient_name = request.user.username
            review.save()
            return redirect('dashboard_patient')
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def specialist_reviews(request):
    reviews = Review.objects.filter(appointment__specialist=request.user.profile).order_by('-date_created')
    return render(request, 'specialist_reviews.html', {'reviews': reviews})

@login_required
def manage_availability(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            availability = form.save(commit=False)
            availability.specialist = request.user.profile
            availability.save()
            return redirect('specialist_dashboard')
    else:
        form = AvailabilityForm()
    return render(request, 'manage_availability.html', {'form': form})

def search_available_appointments(request):
    if request.method == 'GET' and 'date' in request.GET:
        search_date = request.GET['date']
        search_specialization = request.GET.get('specialization', None)
        date_obj = datetime.strptime(search_date, '%Y-%m-%d').date()
        
        if search_specialization:
            available_appointments = Availability.objects.filter(
                start_time__date=date_obj, 
                specialist__specialization=search_specialization
            ).order_by('start_time')
        else:
            available_appointments = Availability.objects.filter(
                start_time__date=date_obj
            ).order_by('start_time')
        
        return render(request, 'search_results.html', {'availabilities': available_appointments, 'search_date': search_date})
    else:
        return render(request, 'search_appointments.html')

