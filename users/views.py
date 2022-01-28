from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader

from events.models import Event
from users.forms import UserRegistrationForm, ProfileRegistrationForm, VolunteerRegistrationForm
from users.models import Profile


def homepage(request):
    events = Event.objects.filter(gps_coordinates_lat__isnull=False, gps_coordinates_long__isnull=False)
    context = {'events': events}
    return render(request, 'index.html', context)


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
                [user.email],
                html_message=loader.render_to_string('users/welcome_html.html',
                                                     {'user_name': 'Welcome' + ' ' + user.first_name,
                                                      'subject': 'We are glad you care about others and chose to be part of our community! '})
            )

            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'An error has occurred during registration')

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
            subject,  # the subject of the mail
            message,  # the message of the mail
            'helpasoul24@gmail.com',
            ['m.sergiu01@gmail.com'],
        )
        print('mail was sent')
        return render(request, 'users/contact_us.html', {'subject': subject})

    return render(request, 'users/contact_us.html')


def become_volunteer(request, pk):
    user = request.user
    profile = Profile.objects.get(user=user)
    event_id = Event.objects.get(pk=pk)
    form = VolunteerRegistrationForm()
    if request.method == 'POST':
        form = VolunteerRegistrationForm(request.POST)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.profile = profile
            volunteer.event_id = event_id
            volunteer.save()
            form.save_m2m()
            return redirect('home_page')
    context = {'form': form}
    return render(request, 'users/volunteer.html', context)
