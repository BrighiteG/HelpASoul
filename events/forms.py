from django import forms
from django.forms import TextInput, DateInput, CheckboxSelectMultiple

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'event_tags', 'profile_image']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adaugă titlul evenimentului', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adaugă descrierea evenimentului', 'class': 'form-control'}),
            'start_date': DateInput(format='%d-%m-%y',
                                    attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de început',
                                           'type': 'date'}),
            'end_date': DateInput(format='%d-%m-%y',
                                  attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de final',
                                         'type': 'date'}),
            'event_tags': CheckboxSelectMultiple(),

        }
