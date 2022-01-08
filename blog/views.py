from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from blog.forms import BlogForm
from blog.models import Blog
from events.models import Tag
from users.models import Profile


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


class BlogDetailView(DetailView):
    template_name = 'blogs/blog_detail_view.html'
    model = Blog


class BlogDeleteView(DeleteView):
    template_name = 'blogs/blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog-list')
