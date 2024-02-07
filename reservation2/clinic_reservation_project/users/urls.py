from django.urls import path
from . import views
from .views import specialist_profile

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    # Dodajemy nowe ścieżki
    path('dashboard_patient/', views.dashboard_patient, name='dashboard_patient'),
    path('specialist_list/', views.specialist_list, name='specialist_list'),
    path('specialist/<int:specialist_id>/', specialist_profile, name='specialist_profile'),

]
