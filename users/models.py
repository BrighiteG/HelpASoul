from typing import TYPE_CHECKING
from django.contrib.auth.models import User
from django.db import models


if TYPE_CHECKING:
    from events.models import Tag
    from social_cases.models import SocialCase


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone_nr = models.IntegerField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    is_volunteer = models.BooleanField(default=False)
    profile_tags = models.ManyToManyField('events.Tag')

    def __str__(self):
        return f"{self.user.first_name}, {self.user.last_name}"


class Review(models.Model):
    social_case = models.ForeignKey('social_cases.SocialCase', on_delete=models.CASCADE, null=True, blank=True)
    blog_comment = models.ForeignKey('blog.Blog', related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    event_comment = models.ForeignKey('events.Event', on_delete=models.CASCADE, null=True, blank=True)
    name = models.TextField(max_length=100, null=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Volunteer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    volunteer_tags = models.ManyToManyField('events.Tag')
    event_id = models.ForeignKey('events.Event', on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.user_id.first_name
