from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from social_cases.forms import SocialCaseForm
from social_cases.models import SocialCase


class SocialCasesListView(ListView):
    template_name = 'social_cases/social_cases_list.html'
    model = SocialCase
    context_object_name = 'social_cases_list'


class SocialCaseUpdateView(UpdateView):
    template_name = 'social_cases/social_case_update.html'
    model = SocialCase
    succses_url = ""
    form_class = SocialCaseForm
