from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from events.forms import EventForm
from events.models import Event
from django.views.generic import TemplateView

from users.models import Profile


class HomeTemplateView(TemplateView):
    template_name = 'base.html'


def event_create(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.profile = profile
            event.save()
            return redirect('events-list')
    context = {'form': form}
    return render(request, 'events/event_create.html', context)


class EventsListView(ListView):
    template_name = 'events/events_list.html'
    model = Event
    context_object_name = 'events_list'


class EventUpdateView(UpdateView):
    template_name = 'events/event_update.html'
    success_url = 'events-list'
    model = Event
    form_class = EventForm


class EventDeleteView(DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    success_url = reverse_lazy('events-list')
