from django.shortcuts import render, redirect

from blog.forms import BlogForm
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
    return render(request, 'blog/blog_create.html', context)

