from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm, ProfileRegistrationForm


def register_user(request):
    page = 'create-user'
    if request.method == 'GET':
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    else:
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            profile.user = user
            profile.save()
            messages.success(request, 'Your account has been created succesfully')

            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'page': page, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/create_user.html', context)


