from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm

def posts_list_view(request):
    posts = Post.objects.filter(status='pub')
    context = {'posts': posts}

    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}

    return render(request, 'blog/post_detail.html',  context)

def create_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = NewPostForm()

    return render(request, 'blog/create_post.html', context={'form': form})
