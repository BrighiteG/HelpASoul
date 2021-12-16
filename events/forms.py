from django import forms
from django.forms import TextInput, DateInput

from events.models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_date', 'end_date', 'tags']
        tag_options = (
            ('Sănătate', 'Healthcare'),
            ('Mediu', 'Environment'),
            ('Familie', 'Family'),
            ('Educație', 'Education')
        )
        widgets = {
            'title': TextInput(attrs={'placeholder': 'Adaugă titlul evenimentului', 'class': 'form-control'}),
            'description': TextInput(attrs={'placeholder': 'Adaugă descrierea evenimentului', 'class': 'form-control'}),
            'start_date': DateInput(format=('%d-%m-%y'),
                                    attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de început'}),
            'end_date': DateInput(format=('%d-%m-%y'),
                                  attrs={'class': 'myDateClass', 'placeholder': 'Selectați data de final'}),
            'tags': forms.CheckboxSelectMultiple(choices='tag_options')
        }