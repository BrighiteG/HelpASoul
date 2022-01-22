from django.contrib import admin

from users.models import Profile, Review, Volunteer

admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Volunteer)
