from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog
from events.models import Tag
from social_cases.forms import ReviewForm
from users.models import Profile, Review


def blog_create(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.profile = profile
            blog.save()
            return redirect('blog-list')
    context = {'blog_form': form}
    return render(request, 'blogs/blog_create.html', context)


def blog_list_view(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    blog_tags = Tag.objects.filter(name__icontains=search_query)
    blog = Blog.objects.distinct().filter(Q(title__icontains=search_query) |
                                          Q(description__icontains=search_query),
                                          Q(blog_tags__in=blog_tags)
                                          )
    context = {'blog_list': blog, 'search_query': search_query}
    return render(request, 'blogs/blog_list.html', context)


def blog_detail_view(request, pk):
    blog = Blog.objects.get(id=pk)
    comments = Review.objects.filter(blog_comment_id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        comment = form.save(commit=False)
        comment.blog_comment = blog
        comment.save()
        return redirect('blog-detail-view', pk=blog.id)
    context = {'blog': blog, 'form': form, 'comments': comments}
    return render(request, 'blogs/blog_detail_view.html', context)


class BlogDeleteView(DeleteView):
    template_name = 'blogs/blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog-list')
