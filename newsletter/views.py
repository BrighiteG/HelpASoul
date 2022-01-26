from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from users.models import Profile
from .models import Subscriber
from .forms import SubscriberForm, Newsletterform
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email='helpasoul24@gmail.com',
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                       sub.email,
                                                       sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        sg.send(message)
        return render(request, 'newsletter/user_subscribe.html',
                      {'email': sub.email, 'action': 'added', 'form': SubscriberForm})
    else:
        return render(request, 'newsletter/user_subscribe.html', {'form': SubscriberForm})


def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'newsletter/user_subscribe.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'newsletter/user_subscribe.html', {'email': sub.email, 'action': 'denied'})


def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'newsletter/user_subscribe.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'newsletter/user_subscribe.html', {'email': sub.email, 'action': 'denied'})


def send_newsletter(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = Newsletterform()
    if request.method == 'POST':
        form = Newsletterform(request.POST)
        if form.is_valid():
            newsletter = form.save(commit=False)
            newsletter.profile = profile

        newsletter_tags = form.cleaned_data['newsletter_tag']
        subscribers_email = Subscriber.objects.filter(subscriber_tags__in=newsletter_tags).values_list('email', flat=True)
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

        for sub in subscribers_email:
            message = Mail(
                from_email='helpasoul24@gmail.com',
                to_emails=sub,
                subject=newsletter.subject,
                html_content=newsletter.contents + (
                    '<br><a href="{}?email={}&conf_num={}">Unsubscribe</a>.').format(
                    request.build_absolute_uri('/delete/'),
                    "sub.email",
                    "sub.conf_num"))

            sg.send(message)
            print(f'MESSAGE SENT SUCCESFULLY TO {sub}')
    context = {'form': form}

    return render(request, 'newsletter/newsletter_create.html', context)
