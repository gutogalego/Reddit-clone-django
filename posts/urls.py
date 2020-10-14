###
# Libraries
###
from django.conf.urls import url, include
from . import views

###
# URLs
###
urlpatterns = [
    url(r'^$', views.post_list, name='posts_list'),
    url(r'^create/$', views.post_create),
    url(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
]
