from django.urls import path

from users import views

urlpatterns = [
    path('create_user/', views.register_user, name='create-user'),
    path('contact_us/', views.contact_us, name='contact-us'),
    path('contact_us_success/', views.contact_us_success, name='contact-us-success'),

]

