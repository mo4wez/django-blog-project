from django.urls import path
from .views import posts_list_view, post_detail_view, create_post_view, update_post_view, delete_post_view

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    path('<int:pk>/', post_detail_view, name='post_detail'),
    path('create/', create_post_view, name='create_post'),
    path('<int:pk>/update', update_post_view, name='post_update'),
    path('<int:pk>/delete', delete_post_view, name='post_delete'),
]
