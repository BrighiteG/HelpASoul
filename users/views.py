from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegistrationForm


class CreateUserCreateView(CreateView):
    template_name = 'users/create_user.html'
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy('homepage')


