from django.urls import path
from .views import posts_list_view, post_detail_view

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    
    # primary key
    path('<int:pk>/', post_detail_view, name='post_detail'),
]
