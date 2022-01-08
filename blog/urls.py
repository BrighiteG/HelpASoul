from django.urls import path

from blog import views

urlpatterns = [
    path('blog_list/', views.blog_list_view, name='blog-list'),
    path('blog_create/', views.blog_create, name='blog-create'),
    path('blog_delete/<int:pk>/', views.BlogDeleteView.as_view(), name='blog-delete'),
    path('blog_detail_view/<int:pk>/', views.BlogDetailView.as_view(), name='blog-detail-view')
]