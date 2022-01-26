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
    organisation = models.CharField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='static/images/dynamic', default='static/images/Aesthetic-Desktop-Wallpaper.jpg')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200, null=True, blank=False)
    gps_coordinates_long = models.DecimalField(max_digits=20, decimal_places=8, default=10.00000000)
    gps_coordinates_lat = models.DecimalField(max_digits=20, decimal_places=8, default=10.00000000)
    event_tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)


class Participant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    is_participant = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.first_name