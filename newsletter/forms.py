from django import forms

from newsletter.models import Newsletter, Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email', 'subscriber_tags']


class Newsletterform(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['subject', 'contents', 'newsletter_tag']

