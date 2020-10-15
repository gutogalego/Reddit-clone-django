from django.contrib import admin

# Register your models here.
from .models import Topic


class TopicModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created_at", "last_updated", "author"]
    list_filter = ["name"]
    search_fields = ["name"]

    class Meta:
        model = Topic


admin.site.register(Topic, TopicModelAdmin)
