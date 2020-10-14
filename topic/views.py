from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
from .models import Topic
from .forms import TopicForm


def topic_create(request):
    form = TopicForm(request.POST or None)

    username = "Not logged in"
    if request.user.is_authenticated:
        username = request.user.username

    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "page_title": "Create Topic",
        "form": form,
        "username": username
    }
    return render(request, "topic/topic_form.html", context)


def topic_detail(request, url_name=None):
    instance = get_object_or_404(Topic, url_name=url_name)
    context = {
        "title": instance.name,
        "instance": instance
    }
    return render(request, "topic/topic_detail.html", context)


def topic_list(request):
    return HttpResponse("<h1>list</h1>")


def topic_update(request):
    return HttpResponse("<h1>update</h1>")


def topic_delete(request):
    return HttpResponse("<h1>delete</h1>")