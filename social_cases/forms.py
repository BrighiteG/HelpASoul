from django import forms
from django.forms import TextInput, CheckboxSelectMultiple, Textarea, SelectMultiple, RadioSelect, FileInput, \
    NumberInput

from social_cases.models import SocialCase
from users.models import Review


class SocialCaseForm(forms.ModelForm):
    class Meta:
        model = SocialCase
        fields = ['title', 'description', 'organisation', 'case_tags', 'profile_image', 'target_donation']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adauga titlul cazului social'}),
            'description': Textarea(attrs={'placeholder': 'Adauga descrierea cazului social'}),
            'organisation': TextInput(attrs={'placeholder': 'Adauga numele organizatiei'}),
            'case_tags': CheckboxSelectMultiple(attrs={'class': 'input'}),
            'profile_image': FileInput(attrs={'placeholder': 'Adaugati o poza cazului social'}),
            'target_donation': NumberInput()
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'body']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Adauga numele tau', 'class': 'form-control'}),
            'body': Textarea(attrs={'placeholder': 'Adauga Comentariul', 'class': 'form-control'})
        }

# class DonationForm(forms.ModelForm):
#     class Meta:
#         model = Donation
#         fields = ['target_donation']
#         widgets = {
#             'target_donation': NumberInput()
#         }
