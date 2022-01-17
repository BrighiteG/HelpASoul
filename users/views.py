from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm, ProfileRegistrationForm


def homepage(request):
    return render(request, 'index.html')


def register_user(request):
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

            subject = 'Welcome to HelpASoul'
            message = 'We are glad you care about others and chose to be part of our community!'
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email]
            )

            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'users/create_user.html', context)


def about_us(request):
    return render(request, 'users/about_us.html')


def gallery(request):
    return render(request, 'users/gallery.html')


def contact_us(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject, #the subject of the mail
            message,  # the message of the mail
            'helpasoul24@gmail.com',
            ['m.sergiu01@gmail.com'],
        )
        print('mail was sent')
        return render(request, 'users/contact_us.html', {'subject': subject})

    return render(request, 'users/contact_us.html')




