from django.shortcuts import render
from django.views.generic import ListView

from social_cases.models import SocialCase


class SocialCasesListView(ListView):
    template_name = 'social_cases/social_cases_list.html'
    model = SocialCase
    context_object_name = 'social_cases_list'

