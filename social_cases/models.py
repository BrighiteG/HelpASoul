from django.contrib.auth.models import User
from django.db import models
from events.models import Tag


class SocialCase(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    # profile_image = models.ImageField()
    donations = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return str(self.title)


