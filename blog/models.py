from django.db import models
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(to='auth.User', on_delete=models.CASCADE)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])
    