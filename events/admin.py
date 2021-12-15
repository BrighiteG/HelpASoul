from django.contrib import admin

from events.models import Events, Tag

admin.site.register(Events)
admin.site.register(Tag)
