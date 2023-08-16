from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/create_post.html'

class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('posts_list')
