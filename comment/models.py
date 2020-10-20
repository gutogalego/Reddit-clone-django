from django.db import models
from django.urls import reverse
from posts.models import Post
from django.conf import settings
from django.shortcuts import render, get_object_or_404
# Create your models here.


class Comment(models.Model):
    content = models.TextField(max_length=300)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"topic": self.post.topic, "id": self.post.id})

    class Meta:
        ordering = ['-created_at', "-last_updated"]
