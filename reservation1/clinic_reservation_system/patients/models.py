from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    pesel = models.CharField(max_length=11)
    phone_number = models.CharField(max_length=15)

