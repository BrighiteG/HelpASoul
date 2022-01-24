from django.contrib import admin
from django.urls import path
from newsletter import views


urlpatterns = [

    path('new/', views.new, name='new'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),
    path('send-newsletter/', views.send_newsletter, name='send-newsletter'),

]
