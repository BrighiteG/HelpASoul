from django import forms
from django.forms import TextInput, CharField, MultipleChoiceField, CheckboxSelectMultiple

from social_cases.models import SocialCase


class SocialCaseForm(forms.ModelForm):
    class Meta:
        tag_options = (
            ('Healthcare', 'Healthcare'),
            ('Environment', 'Environment'),
            ('Animals', 'Animals'),
            ('Family', 'Family'),
        )
        model = SocialCase
        fields = ['title', 'description', 'tag']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adauga titlul cazului social', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adauga descrierea cazului social', 'class': 'form-control'}),
            'tag': CheckboxSelectMultiple(choices=tag_options)
        }




