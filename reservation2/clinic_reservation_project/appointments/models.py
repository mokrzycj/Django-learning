from django.utils import timezone
from django.db import models
from users.models import Profile
import uuid
# from .models import Appointment

# class Appointment(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     patient = models.ForeignKey(Profile, related_name='appointments_as_patient', on_delete=models.CASCADE)
#     specialist = models.ForeignKey(Profile, related_name='appointments_as_specialist', on_delete=models.CASCADE)
#     date = models.DateTimeField()
#     status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

#     def __str__(self):
#         return f"{self.specialist.user.username} - {self.date.strftime('%Y-%m-%d %H:%M')}"

# class Appointment(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     patient = models.ForeignKey(Profile, related_name='appointments', on_delete=models.CASCADE)
#     specialist = models.ForeignKey(Profile, related_name='appointments_as_specialist', on_delete=models.CASCADE)
#     date = models.DateField()
#     time = models.TimeField()
#     status = models.CharField(max_length=20, default='pending')  # Możliwe wartości: pending, confirmed, canceled

    # def __str__(self):
    #     return f"Wizyta u {self.specialist.user.username} dnia {self.date} o godzinie {self.time}"

class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Profile, related_name='appointments', on_delete=models.CASCADE)
    specialist = models.ForeignKey(Profile, related_name='appointments_as_specialist', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending')  # Możliwe wartości: pending, confirmed, canceled
    # date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment {self.id}"


# class Review(models.Model):
#     appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
#     rating = models.IntegerField()
#     comment = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return f"Review for {self.appointment.specialist.user.username} by {self.appointment.patient.user.username}"

class Review(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    patient_name = models.CharField(max_length=100, blank=True, null=True)  # Opcjonalne pole dla nazwy pacjenta
    verified = models.BooleanField(default=False)  # Pole wskazujące, czy opinia została zweryfikowana przez administratora

    def __str__(self):
        return f"Opinia dla {self.appointment.specialist.user.username}"


# Nowy model dla dostępności specjalisty
class Availability(models.Model):
    specialist = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.specialist.user.username} dostępność {self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%H:%M')}"

