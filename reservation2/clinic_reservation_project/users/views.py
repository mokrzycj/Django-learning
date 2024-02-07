from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from appointments.models import Appointment
from django.shortcuts import render, get_object_or_404
from .models import Profile
from appointments.models import Availability, Review

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_patient')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Konto zostało pomyślnie utworzone')
            return redirect('user_login')
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def dashboard_patient(request):
    appointments = Appointment.objects.filter(patient=request.user.profile, status='pending').order_by('date')
    return render(request, 'dashboard_patient.html', {'appointments': appointments})

@login_required
def specialist_list(request):
    query = request.GET.get('q')
    if query:
        specialists = Profile.objects.filter(is_specialist=True, user__username__icontains=query).order_by('user__username')
    else:
        specialists = Profile.objects.filter(is_specialist=True).order_by('user__username')
    return render(request, 'specialist_list.html', {'specialists': specialists})

def specialist_profile(request, specialist_id):
    specialist = get_object_or_404(Profile, pk=specialist_id, is_specialist=True)
    availabilities = Availability.objects.filter(specialist=specialist).order_by('start_time')
    reviews = Review.objects.filter(appointment__specialist=specialist)
    return render(request, 'specialist_profile.html', {'specialist': specialist, 'availabilities': availabilities, 'reviews': reviews})
