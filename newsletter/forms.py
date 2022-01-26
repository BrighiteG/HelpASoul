from django import forms
from django.forms import CheckboxSelectMultiple, TextInput

from newsletter.models import Newsletter, Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'subscriber_tags']
        widgets = {
            'subscriber_tags': CheckboxSelectMultiple(attrs={'class': 'thm-btn dynamic-radius'}),
            'email': TextInput(attrs={'placeholder': 'Enter your email here'})
        }


class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'contents', 'newsletter_tag']

