from django import forms
from django.forms import TextInput, CheckboxSelectMultiple

from social_cases.models import SocialCase


class SocialCaseForm(forms.ModelForm):
    class Meta:
        model = SocialCase
        fields = ['title', 'description', 'tags']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adauga titlul cazului social', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adauga descrierea cazului social', 'class': 'form-control'}),
            'tags': CheckboxSelectMultiple(),
        }




