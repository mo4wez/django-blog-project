from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post
from .forms import NewPostForm

def posts_list_view(request):
    posts = Post.objects.filter(status='pub').order_by('-datetime_modified')
    context = {'posts': posts}

    return render(request, 'blog/posts_list.html', context)

def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)

def create_post_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    else:
        form = NewPostForm()

    return render(request, 'blog/create_post.html', context={'form': form})

def update_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('posts_list')

    return render(request, 'blog/create_post.html', context={'form': form})

def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts_list')

    return render(request, 'blog/delete_post.html', context={'post': post})
