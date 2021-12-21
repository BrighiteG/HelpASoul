from django.urls import path

from users import views

urlpatterns = [
    path('create_user/', views.register_user, name='create-user')
]

