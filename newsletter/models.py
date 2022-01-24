from typing import TYPE_CHECKING

from django.db import models
from sendgrid import SendGridAPIClient, Mail
from HelpASoul import settings
from users.models import Profile
if TYPE_CHECKING:
    from events.models import Tag


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)
    subscriber_tags = models.ManyToManyField('events.Tag')

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    newsletter_tag = models.ManyToManyField('events.Tag')
    contents = models.TextField()

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")

