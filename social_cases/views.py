from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from social_cases.forms import SocialCaseForm
from social_cases.models import SocialCase


class SocialCasesListView(ListView):
    template_name = 'social_cases/social_cases_list.html'
    model = SocialCase
    context_object_name = 'social_cases_list'


class SocialCaseUpdateView(UpdateView):
    template_name = 'social_cases/social_case_update.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')
    form_class = SocialCaseForm


class SocialCaseCreateView(CreateView):
    template_name = 'social_cases/social_case_create.html'
    model = SocialCase
    form_class = SocialCaseForm
    success_url = reverse_lazy('social-cases')


class SocialCaseDeleteView(DeleteView):
    template_name = 'social_cases/social_case_delete.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')





