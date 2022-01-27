from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView

from HelpASoul import settings
from HelpASoul.settings import STRIPE_SECRET_KEY
from events.models import Tag
from newsletter.models import Subscriber
from social_cases.forms import SocialCaseForm, ReviewForm
from social_cases.models import SocialCase
from django.db.models import Q
from users.models import Profile, Review
from .utils import paginate_social_cases
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def social_case_create(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = SocialCaseForm()
    if request.method == "POST":
        form = SocialCaseForm(request.POST, request.FILES)
        if form.is_valid():
            social_case = form.save(commit=False)
            social_case.profile = profile
            social_case.save()
            form.save_m2m()
            social_case = SocialCase.objects.latest('created')
            tags = social_case.case_tags.all()
            subscribers = Subscriber.objects.filter(subscriber_tags__in=tags)

            for sub in subscribers:
                send_mail(
                    subject=f"A new social case has been added ",
                    message=f'Title: {social_case.title} \n Description: {social_case.description}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[sub.email],
                    html_message=
                    (social_case.title + social_case.description)
                    + ('<br><a href="{}?email={}&conf_num={}">If you wish to unsubscribe please click this link</a>.').format(
                        request.build_absolute_uri('/delete/'),
                        sub.email,
                        sub.conf_num),
                )

            return redirect('social-cases')
    context = {'form': form}
    return render(request, 'social_cases/social_case_create.html', context)


def social_case_list_view(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    social_cases = SocialCase.objects.distinct().filter(Q(title__icontains=search_query) |
                                                        Q(description__icontains=search_query) |
                                                        Q(case_tags__in=tags))
    social_cases_with_percentages = []
    for social_case in social_cases:
        percent = social_case.percent_raised()
        amount_raised = social_case.total_donations()
        social_cases_with_percentages.append(
            {'social_case': social_case, 'percent': percent, 'amount_raised': amount_raised})

    custom_range, social_cases_with_percentages = paginate_social_cases(request, social_cases_with_percentages, 3)

    context = {
        'socialcase': social_cases,
        'search_query': search_query,
        'custom_range': custom_range,
        'social_cases_with_percentages': social_cases_with_percentages
        # 'social_cases_with_donation': social_cases_with_donation,
    }

    return render(request, 'social_cases/social_cases_list.html', context)


class SocialCaseUpdateView(UpdateView):
    template_name = 'social_cases/social_case_update.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')
    form_class = SocialCaseForm


class SocialCaseDeleteView(DeleteView):
    template_name = 'social_cases/social_case_delete.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')


def social_case_detail(request, pk):
    social_case = SocialCase.objects.get(id=pk)
    comments = Review.objects.filter(social_case_id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        comment = form.save(commit=False)
        comment.social_case = social_case
        comment.save()

        return redirect('social_case_detail', pk=social_case.id)
    percent = social_case.percent_raised()
    amount_raised = social_case.total_donations()
    context = {'socialcase': social_case, 'form': form, 'comments': comments, 'percent': percent,
               'amount_raised': amount_raised}
    return render(request, 'social_cases/social_case_detail_view.html', context)


def index(request):
    return render(request, 'stripe/index1.html')


def charge(request):
    if request.method == 'POST':
        amount = int(request.POST['amount'])
        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Donation"
        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'stripe/success.html', {'amount': amount})
