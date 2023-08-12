from django.shortcuts import render
from .models import Post

def posts_list_view(request):
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'blog/post_list.html', context)
