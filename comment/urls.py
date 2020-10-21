###
# Libraries
###
from django.conf.urls import url
from . import views

###
# URLs
###
urlpatterns = [
    url(r'^(?P<topic>\w+)/(?P<post_id>\d+)/(?P<comment_id>\d+)/edit/$', views.comment_update, name='comment_update'),
    url(r'^(?P<topic>\w+)/(?P<post_id>\d+)/(?P<comment_id>\d+)/delete/$', views.comment_delete, name='comment_delete'),
]
