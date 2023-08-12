from django.urls import path
from .views import posts_list_view

urlpatterns = [
    path('', posts_list_view, name='posts_list')
]
