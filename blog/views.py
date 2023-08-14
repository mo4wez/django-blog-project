from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Post

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
        post_title = request.POST.get('title')
        post_text = request.POST.get('text')

        user = User.objects.all()[0]
        Post.objects.create(title=post_title, text=post_text, author=user, status='pub')


    return render(request, 'blog/create_post.html')