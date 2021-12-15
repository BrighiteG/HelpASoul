from django.contrib.auth.models import User
from django.db import models


class Events(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizer = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    # profile_image = models.ImageField(upload_to = 'static')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    tag = models.ManyToManyField('events.Tag')

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    name = models.CharField(max_length=200)
    social_case_organizer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
