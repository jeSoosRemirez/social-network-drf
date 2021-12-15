from django.urls import path
from posts.views import PostDetailView, PostListView, api_root, PostCreateView, PostLikeView, AnalyticView
from rest_framework.urlpatterns import format_suffix_patterns


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', PostLikeView.as_view()),
    path('api/analytics/', AnalyticView.as_view()),
])
