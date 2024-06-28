from django import forms
from .models import Libro
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username","password"]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1", "password2"]