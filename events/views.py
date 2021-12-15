from django.shortcuts import render
from django.views.generic import ListView

from events.models import Events


from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


class EventsListView(ListView):
    template_name = 'events/events_list.html'
    model = Events
    context_object_name = 'events_list'

