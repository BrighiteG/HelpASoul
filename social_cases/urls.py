from django.urls import path

from social_cases import views

urlpatterns = [
    path('social_cases_list', views.SocialCasesListView.as_view(), name='social-cases'),
    path('social_case_update/<int:pk>/', views.SocialCaseUpdateView.as_view(), name='update-social-case'),
    path('social_case_create/', views.SocialCaseCreateView.as_view(), name='create-social-case'),
    path('social_case_delete/<int:pk>/', views.SocialCaseDeleteView.as_view(), name='delete-social-case')
]


