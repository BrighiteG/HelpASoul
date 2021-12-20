from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Introduceți prenumele dvs.', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Introduceți numele dvs.', 'class': 'form-control'}),
            'email': TextInput(attrs={'placeholder': 'Introduceți adresa de email', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Introduceți username-ul dorit', 'class': 'form-control'}),
        }

