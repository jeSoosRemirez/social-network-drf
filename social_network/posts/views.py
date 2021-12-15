from collections import Counter
from itertools import groupby
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView, get_object_or_404, \
    GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from posts.models import Post, Like
from posts.serializers import PostListSerializer, PostDetailSerializer, PostCreateSerializer, AnalyticsSerializer
from users.backends import JWTAuthentication
from datetime import datetime


class PostCreateView(CreateAPIView):
    """
    This APIView provides `create` action
    with 'owner', 'text', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        # The request user is set as owner automatically.
        serializer.save(owner=self.request.user)


class PostListView(ListAPIView):
    """
    This APIView provides `list` action
    with 'owner', 'text', 'likes', 'dislikes', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """
    This APIView provides `list` action
    with 'id', 'owner', 'text', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostLikeView(APIView):

    def get(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, id=pk)
            if request.user in post.liked_by.all():
                post.liked_by.remove(request.user)
            else:
                post.liked_by.add(request.user)
            post.save()
            return Response({'success': True})
        else:
            return Response({'success': False})


class AnalyticView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Like.objects.all()
    serializer_class = AnalyticsSerializer

    def get_queryset(self, date_from, date_to):
        date_from = datetime.strptime(date_from, '%Y-%m-%d')
        date_to = datetime.strptime(date_to, '%Y-%m-%d')
        queryset = Like.objects.filter(created_time__gte=date_from, created_time__lte=date_to).order_by('created_time')
        return queryset

    def get(self, request):
        queryset = self.get_queryset(request.query_params['date_from'], request.query_params['date_to'])
        filtered_queryset = self.filter_queryset(queryset)
        likes_by_date = groupby(filtered_queryset,
                                lambda like: like.created_time.strftime("%Y-%m-%d"))

        analytics = []
        for date, likes in likes_by_date:
            count = Counter(like.post_id for like in likes)
            analytics.append(
                {
                    'date': date,
                    'total_likes': sum(count.values()),
                }
            )

        return Response(analytics)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Posts api roots
        'posts': reverse('post-list', request=request, format=format),
        'post-create': reverse('post-create', request=request, format=format),

        # Users api roots
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'update': reverse('update', request=request, format=format),
    })
