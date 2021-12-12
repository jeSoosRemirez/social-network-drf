from django.db import models


class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='social_network_app', on_delete=models.CASCADE)
    text = models.TextField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_time']
