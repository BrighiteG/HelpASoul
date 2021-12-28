from django.urls import path

from social_cases import views

urlpatterns = [
    path('social_cases_list/', views.social_case_list_view, name='social-cases'),
    path('social_case_update/<int:pk>/', views.SocialCaseUpdateView.as_view(), name='update-social-case'),
    path('social_case_create/', views.social_case_create, name='create-social-case'),
    path('social_case_delete/<int:pk>/', views.SocialCaseDeleteView.as_view(), name='delete-social-case'),
    path('social_case_detail/<int:pk>/', views.SocialCaseDetailView.as_view(), name='social_case_detail')
]


