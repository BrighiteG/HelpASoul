from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, CheckboxSelectMultiple, Textarea
from users.models import Profile, Volunteer


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
            # 'profile_tags': CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }


class VolunteerRegistrationForm(forms.ModelForm):
    # volunteer_tags = forms.MultipleChoiceField(label="Alege ariile de interes: ")

    class Meta:
        model = Volunteer
        fields = ['volunteer_tags', 'message']

        widgets = {
            'volunteer_tags': CheckboxSelectMultiple(),
            'message': Textarea(attrs={'placeholder': 'Spune-ne cum poți ajuta'})
        }

    def __init__(self, *args, **kwargs):
        super(VolunteerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['volunteer_tags'].label = 'Alege ariile de interes'
