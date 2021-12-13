from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from posts.models import Post
from posts.serializers import PostListSerializer, PostDetailSerializer
from users.backends import JWTAuthentication


class PostListView(ListCreateAPIView):
    """
    This APIView provides `list` action
    with 'owner', 'author_email', 'text', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    This APIView provides `list` action
    with 'id', 'author', 'author_email', 'text', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Posts api roots
        'posts': reverse('post-list', request=request, format=format),

        # Users api roots
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'update': reverse('update', request=request, format=format),
    })
