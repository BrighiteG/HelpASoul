from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from events.models import Tag
from social_cases.forms import SocialCaseForm, ReviewForm
from social_cases.models import SocialCase
from django.db.models import Q
from users.models import Profile, Review


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



    page = request.GET.get('page')
    results = 3
    paginator = Paginator(social_cases_with_percentages, results)

    try:
        social_cases_with_percentages = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
        social_cases_with_percentages = paginator.page(page)

    left_index = (int(page) - 4)
    if left_index < 1:
        left_index = 1
    right_index = (int(page) + 5)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {
               'search_query': search_query,
               'paginator': paginator,
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
