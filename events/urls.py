from django.urls import path

from events import views

urlpatterns = [
    path('homepage/', views.HomeTemplateView.as_view(), name='homepage'),
    path('events_list/', views.event_list_view, name='events-list'),
    path('event_update/<int:pk>/', views.EventUpdateView.as_view(), name='event-update'),
    path('event_create/', views.event_create, name='event-create'),
    path('event_delete/<int:pk>/', views.EventDeleteView.as_view(), name='event-delete'),
    path('event_detail_view/<int:pk>/', views.EventDetailView.as_view(), name='event-detail-view')
]
