from typing import TYPE_CHECKING
from django.contrib.auth.models import User
from django.db import models
from users.models import Profile


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='static/images/dynamic', default='static/images/Aesthetic-Desktop-Wallpaper.jpg')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    event_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)



