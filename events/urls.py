from django.urls import path

from events import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('events_list/', views.EventsListView.as_view(), name='events-list'),
    path('event_update/<int:pk>/', views.EventUpdateView.as_view(), name='event-update'),
    path('event_create/', views.EventCreateView.as_view(), name='event-create'),
    path('event_delete/<int:pk>/', views.EventDeleteView.as_view(), name='event-delete')
]
