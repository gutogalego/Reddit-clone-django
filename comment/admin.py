from django.contrib import admin

# Register your models here.
from .models import Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "last_updated"]
    list_filter = ["last_updated", "created_at"]
    search_fields = ["author", "content"]

    class Meta:
        model = Comment


admin.site.register(Comment, CommentModelAdmin)
