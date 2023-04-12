from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post_list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('replies/', views.ReplyList.as_view(), name='reply_list'),
    path('replies/<int:pk>/', views.ReplyDetail.as_view(), name='reply_detail'),
]
