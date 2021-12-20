from django.urls import path

from users import views

urlpatterns = [
    path('create_user/', views.CreateUserCreateView.as_view(), name='create-user')
]