from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'phone', 'username', 'password1', 'password2']
