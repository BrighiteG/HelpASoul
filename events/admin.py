from django.contrib import admin

from events.models import Event, Tag
from users.models import Volunteer

admin.site.register(Event)
admin.site.register(Tag)
