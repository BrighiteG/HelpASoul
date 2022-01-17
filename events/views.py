from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView


from events.forms import EventForm
from events.models import Event, Tag
from django.views.generic import TemplateView

from social_cases.forms import ReviewForm
from users.models import Profile, Review
from .utils import search_events, paginate_events


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
            form.save_m2m()
            return redirect('events-list')
    context = {'form': form}
    return render(request, 'events/event_create.html', context)


def event_list_view(request):
    events, search_query = search_events(request)
    custom_range, events = paginate_events(request, events, 2)


    context = {'events_list': events, 'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'events/events_list.html', context)



class EventUpdateView(UpdateView):
    template_name = 'events/event_update.html'
    success_url = 'events-list'
    model = Event
    form_class = EventForm


def event_detail_view(request, pk):
    event = Event.objects.get(id=pk)
    comments = Review.objects.filter(event_comment=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        comment = form.save(commit=False)
        comment.event_comment = event
        comment.save()
        return redirect('event-detail-view', pk=event.id)
    context = {'event': event, 'form': form, 'comments': comments}
    return render(request, 'events/event_detail_view.html', context)


class EventDeleteView(DeleteView):
    template_name = 'events/event_delete.html'
    model = Event
    success_url = reverse_lazy('events-list')
