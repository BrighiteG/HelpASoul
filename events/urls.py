from django.urls import path

from events import views

urlpatterns = [
    path('events_list', views.EventsListView.as_view(), name='events-list')
]