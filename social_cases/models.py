from typing import TYPE_CHECKING
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count, Sum

from users.models import Profile, Review

if TYPE_CHECKING:
    from events.models import Tag



class SocialCase(models.Model):
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # organizer = models.TextField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='static/images/', default='static/images/Aesthetic-Desktop-Wallpaper.jpg')
    case_tags = models.ManyToManyField('events.Tag')
    target_donation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    raised = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)


    @property
    def total_donations(self):
        count = SocialCase.objects.aggregate(Sum('raised'))
        return count['raised__sum']


    @property
    def percentage(self):
        raised = self.raised
        if raised is None:
            raised = 0
        target_donation = self.target_donation
        percentage = (raised / target_donation) * 100
        return round(percentage)


    def __str__(self):
        return str(self.title)


# class Donation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     social_case = models.ForeignKey(SocialCase, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return str(self.social_case.title)


