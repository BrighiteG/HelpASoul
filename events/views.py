from django.shortcuts import render
from django.views.generic import ListView

from events.models import Events


class EventsListView(ListView):
    template_name = 'events/events_list.html'
    model = Events
    context_object_name = 'events_list'

