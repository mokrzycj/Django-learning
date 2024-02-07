"""
URL configuration for clinic_reservation_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from patients.views import register_patient
# from specialists.views import register_specialist
# from patients.views import book_appointment, appointments_list, cancel_appointment
# from patients.views import add_review
# from specialists.views import reviews_list
# from clinics.views import add_specialist_to_clinic, clinic_specialists_list, remove_specialist_from_clinic, clinic_appointments_list, cancel_appointment_by_clinic



# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('register/patient/', register_patient, name='register_patient'),
#     path('register/specialist/', register_specialist, name='register_specialist'),
#     path('admin/', admin.site.urls),
#     path('appointments/book/<int:specialist_id>/', book_appointment, name='book_appointment'),
#     path('appointments/', appointments_list, name='appointments_list'),
#     path('appointments/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
#     path('reviews/add/<int:specialist_id>/', add_review, name='add_review'),
#     path('specialist/reviews/', reviews_list, name='reviews_list'),
#     path('clinic/add_specialist/', add_specialist_to_clinic, name='add_specialist_to_clinic'),
#     path('clinic/specialists/', clinic_specialists_list, name='clinic_specialists_list'),
#     path('clinic/remove_specialist/<int:specialist_id>/', remove_specialist_from_clinic, name='remove_specialist_from_clinic'),
#     path('clinic/appointments/', clinic_appointments_list, name='clinic_appointments_list'),
#     path('clinic/appointments/cancel/<int:appointment_id>/', cancel_appointment_by_clinic, name='cancel_appointment_by_clinic'),
# ]

from django.contrib import admin
from django.urls import path
from patients.views import register_patient, book_appointment, appointments_list, cancel_appointment, add_review
from specialists.views import register_specialist, reviews_list
from clinics.views import add_specialist_to_clinic, clinic_specialists_list, remove_specialist_from_clinic, clinic_appointments_list, cancel_appointment_by_clinic

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/patient/', register_patient, name='patients/register'),
    path('register/specialist/', register_specialist, name='specialists/register'),
    path('appointments/book/<int:specialist_id>/', book_appointment, name='book_appointment'),
    path('appointments/', appointments_list, name='appointments_list'),
    path('appointments/cancel/<int:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('reviews/add/<int:specialist_id>/', add_review, name='add_review'),
    path('specialist/reviews/', reviews_list, name='reviews_list'),
    path('clinic/add_specialist/', add_specialist_to_clinic, name='add_specialist_to_clinic'),
    path('clinic/specialists/', clinic_specialists_list, name='clinic_specialists_list'),
    path('clinic/remove_specialist/<int:specialist_id>/', remove_specialist_from_clinic, name='remove_specialist_from_clinic'),
    path('clinic/appointments/', clinic_appointments_list, name='clinic_appointments_list'),
    path('clinic/appointments/cancel/<int:appointment_id>/', cancel_appointment_by_clinic, name='cancel_appointment_by_clinic'),
]

