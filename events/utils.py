from django.db.models import Q

from events.models import Tag, Event


def search_events(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    events = Event.objects.distinct().filter(Q(title__icontains=search_query) |
                                             Q(description__icontains=search_query) |
                                             Q(event_tags__in=tags))

    return events, search_query
