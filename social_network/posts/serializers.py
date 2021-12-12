from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of posts
    """
    class Meta:
        model = Post
        fields = ['owner', 'text', 'created_time']


class PostDetailSerializer(serializers.ModelSerializer):
    """
    Shows when we look at exact post
    """
    class Meta:
        model = Post
        fields = ['id', 'owner', 'text', 'created_time']
