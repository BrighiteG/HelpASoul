from django.urls import path

from social_cases import views

urlpatterns = [
    path('social_cases_list', views.SocialCasesListView.as_view(), name='social-cases'),
    path('social_case_update/<int:pk>/', views.SocialCaseUpdateView.as_view(), name='update-social-case')
]


