from django.contrib import admin

from events.models import Event, Tag

admin.site.register(Event)
admin.site.register(Tag)
