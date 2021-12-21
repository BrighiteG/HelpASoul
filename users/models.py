from typing import TYPE_CHECKING

from django.contrib.auth.models import User
from django.db import models
if TYPE_CHECKING:
    from events.models import Tag



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_nr = models.IntegerField()
    location = models.CharField(max_length=200)
    is_volunteer = models.BooleanField(default=False)
    profile_tags = models.ManyToManyField('events.Tag')

    def __str__(self):
        return str(self.location)
