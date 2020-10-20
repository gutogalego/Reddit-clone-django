from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
from .models import Topic
from .forms import TopicForm


def topic_create(request):
    form = TopicForm(request.POST or None)

    if not request.user.is_authenticated:
        return HttpResponse("<h1>Please log in to create topic</h1>")

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
    topic = get_object_or_404(Topic, url_name=url_name)
    posts_query = topic.posts.all()
    paginator = Paginator(posts_query, 7)  # Show 7 topics per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "title": topic.name,
        "instance": topic,
        "page_obj": page_obj,
    }
    return render(request, "topic/topic_detail.html", context)


def topic_list(request):
    queryset = Topic.objects.all()
    paginator = Paginator(queryset, 7)  # Show 7 topics per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "title": "All Topics:",
        "object_list": queryset,
        'page_obj': page_obj
    }

    return render(request, "topic/topic_list.html", context)


def topic_update(request, url_name=None):
    instance = get_object_or_404(Topic, url_name=url_name)
    form = TopicForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "page_title": "Edit Topic",
        "title": instance.name,
        "instance": instance,
        "form": form
    }
    return render(request, "topic/topic_form.html", context)


def topic_delete(request, url_name=None):
    instance = get_object_or_404(Topic, url_name=url_name)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("topic_list")
