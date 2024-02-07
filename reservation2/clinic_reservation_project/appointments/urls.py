from django.urls import path
from .views import book_appointment
from .views import patient_appointments, specialist_appointments, cancel_appointment, confirm_appointment, add_review, specialist_reviews, manage_availability, search_available_appointments


urlpatterns = [
    path('book/<int:specialist_id>/', book_appointment, name='book_appointment'),
    path('patient/', patient_appointments, name='patient_appointments'),
    path('specialist/', specialist_appointments, name='specialist_appointments'),
    path('cancel/<uuid:appointment_id>/', cancel_appointment, name='cancel_appointment'),
    path('confirm/<uuid:appointment_id>/', confirm_appointment, name='confirm_appointment'),
    path('add_review/<uuid:appointment_id>/', add_review, name='add_review'),
    path('reviews/', specialist_reviews, name='specialist_reviews'),
    path('manage_availability/', manage_availability, name='manage_availability'),
    path('search/', search_available_appointments, name='search_available_appointments'),

]
