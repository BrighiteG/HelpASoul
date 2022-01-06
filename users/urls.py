from django.urls import path

from users import views

urlpatterns = [
    path('create_user/', views.register_user, name='create-user'),
    path('about_us/', views.about_us, name='about-us'),
    path('gallery/', views.gallery, name='gallery')
]

