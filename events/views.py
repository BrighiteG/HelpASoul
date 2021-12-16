from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from events.forms import EventForm
from events.models import Event
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


class EventsListView(ListView):
    template_name = 'events/events_list.html'
    model = Event
    context_object_name = 'events_list'


class EventUpdateView(UpdateView):
    template_name = 'events/event_update.html'
    success_url = 'homepage'
    model = Event
    form_class = EventForm
