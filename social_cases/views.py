from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from social_cases.forms import SocialCaseForm
from social_cases.models import SocialCase
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


class SocialCasesListView(ListView):
    template_name = 'social_cases/social_cases_list.html'
    model = SocialCase
    context_object_name = 'social_cases_list'


class SocialCaseUpdateView(UpdateView):
    template_name = 'social_cases/social_case_update.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')
    form_class = SocialCaseForm


class SocialCaseDeleteView(DeleteView):
    template_name = 'social_cases/social_case_delete.html'
    model = SocialCase
    success_url = reverse_lazy('social-cases')





