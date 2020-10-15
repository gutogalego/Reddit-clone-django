from django.db import models
from django.urls import reverse
from topic.models import Topic
from django.shortcuts import render, get_object_or_404
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField(max_length=10_000)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default="default", related_name='posts')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-timestamp', "-last_updated"]