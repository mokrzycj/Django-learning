from django.shortcuts import render, redirect
from specialists.models import Specialist
from .models import Appointment


def add_specialist_to_clinic(request):
    if request.method == 'POST':
        specialist_email = request.POST.get('specialist_email')
        try:
            specialist = Specialist.objects.get(user__email=specialist_email)
            # Tu zakładamy, że istnieje relacja między modelem Specialist a Clinic
            specialist.clinic = request.user.clinic
            specialist.save()
            return redirect('clinic_specialists_list')
        except Specialist.DoesNotExist:
            pass  # Obsłuż sytuację, gdy specjalista nie istnieje
    return render(request, 'clinics/add_specialist.html')

def clinic_specialists_list(request):
    specialists = Specialist.objects.filter(clinic=request.user.clinic)
    return render(request, 'clinics/specialists_list.html', {'specialists': specialists})

def remove_specialist_from_clinic(request, specialist_id):
    try:
        specialist = Specialist.objects.get(id=specialist_id, clinic=request.user.clinic)
        specialist.clinic = None  # Zakładając, że brak przynależności do przychodni jest oznaczony jako None
        specialist.save()
    except Specialist.DoesNotExist:
        pass  # Obsłuż sytuację, gdy specjalista nie istnieje lub nie należy do przychodni
    return redirect('clinic_specialists_list')
def clinic_appointments_list(request):
    appointments = Appointment.objects.filter(specialist__clinic=request.user.clinic).order_by('date_time')
    return render(request, 'clinics/appointments_list.html', {'appointments': appointments})

def cancel_appointment_by_clinic(request, appointment_id):
    try:
        appointment = Appointment.objects.get(id=appointment_id, specialist__clinic=request.user.clinic)
        appointment.status = 'Cancelled'
        appointment.save()
    except Appointment.DoesNotExist:
        pass  # Obsłuż sytuację, gdy wizyta nie istnieje
    return redirect('clinic_appointments_list')