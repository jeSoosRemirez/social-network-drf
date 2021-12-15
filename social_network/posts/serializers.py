from rest_framework import serializers
from posts.models import Post, Like


class PostCreateSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of posts
    """
    created_time = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ['text', 'created_time']


class PostListSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of posts
    """

    class Meta:
        model = Post
        fields = ['text', 'owner', 'created_time']


class PostDetailSerializer(serializers.ModelSerializer):
    """
    Shows when we look at exact post
    """
    class Meta:
        model = Post
        fields = ['id', 'text', 'created_time']


class AnalyticsSerializer(serializers.ModelSerializer):
    """
    Likes analytic
    """

    class Meta:
        model = Like
        fields = '__all__'
