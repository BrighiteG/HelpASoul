from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, CheckboxSelectMultiple
from users.models import Profile


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

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_nr', 'location', 'profile_tags']
        widgets = {
            'phone_nr': TextInput(attrs={'placeholder': 'Introduceți prenumele dvs.', 'class': 'form-control'}),
            'location': TextInput(attrs={'placeholder': 'Introduceți numele dvs.', 'class': 'form-control'}),
            'profile_tags': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }
