from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class PatientSignUpForm(UserCreationForm):
    pesel = forms.CharField(max_length=11)
    phone_number = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'pesel', 'phone_number',)
