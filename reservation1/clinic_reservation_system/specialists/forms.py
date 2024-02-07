from django import forms
from django.contrib.auth.forms import UserCreationForm
from patients.models import CustomUser

class SpecialistSignUpForm(UserCreationForm):
    specialty = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'specialty', 'phone_number',)
