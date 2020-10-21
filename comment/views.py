from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

from comment.models import Comment
from topic.models import Topic
from comment.forms import CommentForm


def comment_update(request, topic=None, post_id=None, comment_id=None):
    instance = get_object_or_404(Comment, id=comment_id)
    if not request.user == instance.author:
        return HttpResponse("<h1>Only the author can edit</h1>")

    form = CommentForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # message success
        messages.success(request, "Successfully Updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "page_title": "Edit Comment",
        "content": instance.content,
        "instance": instance,
        "form": form
    }
    return render(request, "comment/comment_form.html", context)


def comment_delete(request, topic=None, post_id=None, comment_id=None):
    instance = get_object_or_404(Comment, id=comment_id)
    if request.user == instance.author:
        instance.delete()
        messages.success(request, "Successfully Deleted")
        return redirect("post_detail", topic, post_id)
    else:
        return HttpResponse("<h1>Only the author can delete</h1>")