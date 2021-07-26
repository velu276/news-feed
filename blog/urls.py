from django.urls import path
from . import views
from .views import (
	PostListView, 
	PostDetailView, 
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    MyPostListView,
    UserPostListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('my_home/', MyPostListView.as_view(), name='my-posts'),
    path('my_home/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')
]