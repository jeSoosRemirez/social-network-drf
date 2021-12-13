from django.db import models
from django.conf import settings


class Post(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='social_network_app', on_delete=models.CASCADE)
    text = models.TextField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
