from django.db import models
from django.urls import reverse
from topic.models import Topic
from django.conf import settings
from django.shortcuts import render, get_object_or_404
# Create your models here.


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(max_length=10_000)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default="default", related_name='posts')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    draft = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"topic": self.topic, "id": self.id})

    class Meta:
        ordering = ['-timestamp', "-last_updated"]
