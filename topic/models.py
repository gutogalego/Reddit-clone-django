from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=10_000)
    author = models.CharField(max_length=120)
    url_name = models.SlugField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("list", kwargs={"url_name": self.url_name})
