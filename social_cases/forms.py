from django import forms
from django.forms import TextInput, CheckboxSelectMultiple, Textarea, SelectMultiple, RadioSelect, FileInput

from social_cases.models import SocialCase


class SocialCaseForm(forms.ModelForm):
    class Meta:
        model = SocialCase
        fields = ['title', 'description', 'case_tags', 'profile_image']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adauga titlul cazului social' }),
            'description': Textarea(attrs={'placeholder': 'Adauga descrierea cazului social'}),
            'case_tags': CheckboxSelectMultiple(attrs={'class': 'input'}),
            'profile_image': FileInput(attrs={'placeholder': 'Adaugati o poza cazului social'})
        }





