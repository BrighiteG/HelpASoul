from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.db import models
if TYPE_CHECKING:
    from events.models import Tag


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_nr = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    is_volunteer = models.BooleanField(default=False, null=True, blank=True)
    profile_tags = models.ManyToManyField('events.Tag')

    def __str__(self):
        return str(self.location)


