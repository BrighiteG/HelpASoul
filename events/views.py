from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
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


class EventCreateView(CreateView):
    template_name = 'events/event_create.html'
    model = Event
    success_url = reverse_lazy('events-list')
    form_class = EventForm


class EventDeleteView(DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    success_url = reverse_lazy('events-list')
