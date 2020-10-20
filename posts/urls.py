###
# Libraries
###
from django.conf.urls import url, include
from . import views

###
# URLs
###
urlpatterns = [
    url(r'^all/$', views.post_list, name='posts_list'),
    url(r'^(?P<topic>\w+)/create/$', views.post_create, name='post_create'),
    url(r'^(?P<topic>\w+)/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<topic>\w+)/(?P<id>\d+)/edit/$', views.post_update, name='post_update'),
    url(r'^(?P<topic>\w+)/(?P<id>\d+)/delete/$', views.post_delete, name='post_delete'),
]
