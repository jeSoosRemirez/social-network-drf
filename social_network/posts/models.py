from django.db import models
from django.conf import settings
from users.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.CASCADE)
    text = models.TextField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked', through='Like')

    class Meta:
        ordering = ['created_time']


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
