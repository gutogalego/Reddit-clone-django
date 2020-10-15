from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
from .forms import PostForm
from .models import Post


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "page_title": "Create Post",
        "form": form,
    }
    return render(request, "posts/post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance
    }
    return render(request, "posts/post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(queryset, 7)  # Show 7 posts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "title": "List",
        "object_list": queryset,
        'page_obj': page_obj
    }

    return render(request, "posts/post_list.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "page_title": "Edit Post",
        "title": instance.title,
        "instance": instance,
        "form": form
    }
    return render(request, "posts/post_form.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("list")
