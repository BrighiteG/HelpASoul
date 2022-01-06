from django.db import models

from events.models import Tag
from users.models import Profile


class Blog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True, blank=False)
    profile_image = models.ImageField(upload_to='static/images/dynamic')
    created_at = models.DateTimeField(auto_now_add=True)
    blog_tags = models.ManyToManyField('events.Tag')

    def __str__(self):
        return str(self.title)
