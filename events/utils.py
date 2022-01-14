from django.db.models import Q

from events.models import Tag, Event
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_events(request, events, results):
    page = request.GET.get('page')
    results = 2
    paginator = Paginator(events, results)

    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        events = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        events = paginator.page(page)

    left_index = (int(page) - 1)

    if left_index < 1:
        left_index = 1

    right_index = (int(page) + 2)

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)
    return custom_range, events


def search_events(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    events = Event.objects.distinct().filter(Q(title__icontains=search_query) |
                                             Q(description__icontains=search_query) |
                                             Q(event_tags__in=tags))

    return events, search_query
