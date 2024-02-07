from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_patient = models.BooleanField(default=False)
    is_specialist = models.BooleanField(default=False)
    # Dodatkowe pola specyficzne dla profilu
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True, null=True)
    # Dodajemy do modelu Profile
    specialization = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
