from django.db import models
from patients.models import CustomUser

class Specialist(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    specialty = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
