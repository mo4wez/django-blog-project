from django.urls import path
from .views import posts_list_view, post_detail_view, create_post_view

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    # primary key
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', create_post_view, name='create_post')
]
