from django.urls import path

from social_cases import views

# from social_cases.views import CustomPaymentView, StripeIntentView


urlpatterns = [
    path('social_cases_list/', views.social_case_list_view, name='social-cases'),
    path('social_case_update/<int:pk>/', views.SocialCaseUpdateView.as_view(), name='update-social-case'),
    path('social_case_create/', views.social_case_create, name='create-social-case'),
    path('social_case_delete/<int:pk>/', views.SocialCaseDeleteView.as_view(), name='delete-social-case'),
    path('social_case_detail/<int:pk>/', views.social_case_detail, name='social_case_detail'),
    path('index/', views.index, name="index"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),

]
