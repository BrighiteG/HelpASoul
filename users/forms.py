from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, CheckboxSelectMultiple, Textarea, BooleanField, CheckboxInput
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
        fields = ['location', 'professional_areas', 'is_driver', 'is_available_for_emergengy', 'volunteer_tags',
                  'message']

        widgets = {
            'location': TextInput(attrs={'placeholder': 'ex. Banat/România/Timiș', 'class': 'form-control'}),
            'professional_areas': TextInput(attrs={'placeholder': 'ex. Tâmplărie, Educație, Medicină, Construcții',
                                                   'class': 'form-control'}),
            # 'is_driver': CheckboxInput(),
            # 'is_available_for_emergengy': BooleanField(),
            'volunteer_tags': CheckboxSelectMultiple(),
            'message': Textarea(attrs={'placeholder': 'Mesajul tău aici'})
        }

    def __init__(self, *args, **kwargs):
        super(VolunteerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['location'].label = 'Specifică zona în care poți participa la evenimente'
        self.fields['professional_areas'].label = 'În ce domenii de cunoaștere crezi că ai putea ajuta?'
        self.fields['volunteer_tags'].label = 'Alege ariile de interes'
        self.fields['is_driver'].label = 'Ai mașină și ești disponibil să te deplasezi unde este nevoie?'
        self.fields['is_available_for_emergengy'].label = 'Poți fi contactat pentru situații neprevăzute și neplanificate?'
        self.fields['message'].label = 'Spune-ne cum dorești să te implici și cum și în ce domenii ai putea ajuta'

