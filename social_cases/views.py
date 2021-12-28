from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from events.models import Tag
from social_cases.forms import SocialCaseForm
from social_cases.models import SocialCase
from django.db.models import Q
from users.models import Profile


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

    context = {'social_cases_list': social_cases, 'search_query': search_query}
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

class SocialCaseDetailView(DetailView):
    template_name = 'social_cases/social_case_detail_view.html'
    model = SocialCase





