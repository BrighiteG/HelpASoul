from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, DetailView

from events.forms import EventForm
from events.models import Event, Tag
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


def event_list_view(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    events = Event.objects.distinct().filter(Q(title__icontains=search_query) |
                                             Q(description__icontains=search_query) |
                                             Q(event_tags__in=tags))
    context = {'events_list': events, 'search_query': search_query}
    return render(request, 'events/events_list.html', context)


class EventUpdateView(UpdateView):
    template_name = 'events/event_update.html'
    success_url = 'events-list'
    model = Event
    form_class = EventForm


class EventDeleteView(DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    success_url = reverse_lazy('events-list')


class EventDetailView(DetailView):
    template_name = 'events/event_detail_view.html'
    model = Event
