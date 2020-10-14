###
# Libraries
###
from django.conf.urls import url, include
from . import views

###
# URLs
###
urlpatterns = [
    url(r'^$', views.topic_list, name='topic_list'),
    url(r'^create/$', views.topic_create),
    url(r'^(?P<url_name>\w+)/$', views.topic_detail, name='topic_detail'),
    url(r'^(?P<id>\w+)/edit/$', views.topic_update, name='topic_update'),
    url(r'^(?P<id>\w+)/delete/$', views.topic_delete),
]
