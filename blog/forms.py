from django.forms import ModelForm

from .models import Post

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'status']