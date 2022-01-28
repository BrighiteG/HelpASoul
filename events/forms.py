from django import forms
from django.forms import TextInput, DateInput, CheckboxSelectMultiple, DecimalField

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'organisation', 'start_date', 'end_date',
                  'location', 'gps_coordinates_long', 'gps_coordinates_lat', 'event_tags', 'profile_image']
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adaugă titlul evenimentului', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adaugă descrierea evenimentului', 'class': 'form-control'}),
            'organisation': TextInput(attrs={'placeholder': 'Adaugă numele organizației', 'class': 'form-control'}),
            'start_date': DateInput(format='%d-%m-%y',
                                    attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de început',
                                           'type': 'date'}),
            'end_date': DateInput(format='%d-%m-%y',
                                  attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de final',
                                         'type': 'date'}),
            'location': TextInput(attrs={'placeholder': 'Adaugă adresa: strada / număr / localitate / județ',
                                         'class': 'form-control'}),
            'event_tags': CheckboxSelectMultiple(attrs={'class': "form-check-inline"}),

        }
