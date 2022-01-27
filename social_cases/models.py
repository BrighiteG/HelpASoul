from typing import TYPE_CHECKING
from django.contrib.auth.models import User
from django.db import models
from newsletter.models import Subscriber
from users.models import Profile, Review
if TYPE_CHECKING:
    from events.models import Tag


class SocialCase(models.Model):
    title = models.CharField(max_length=200)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    organisation = models.TextField(max_length=200, null=True, blank=False)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='static/images/', default='static/images/Aesthetic-Desktop-Wallpaper.jpg')
    case_tags = models.ManyToManyField('events.Tag')
    target_donation = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def percent_raised(self):
        total = 0
        for donation in self.donations_so_far.all():
            total += donation.raised
        return round(float(total) * 100 / float(self.target_donation))

    def total_donations(self):
        total = 0
        for donation in self.donations_so_far.all():
            total += donation.raised
        return total

    def __str__(self):
        return str(self.title)


class Donation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    social_case = models.ForeignKey(SocialCase, related_name='donations_so_far', on_delete=models.CASCADE)
    raised = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.social_case.title)



