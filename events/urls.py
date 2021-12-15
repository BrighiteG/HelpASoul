from django.urls import path

from events import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('events_list', views.EventsListView.as_view(), name='events-list')
]
