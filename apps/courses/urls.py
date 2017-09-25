from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^courses/destroy/(?P<id>\d+)$', views.destroy),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete),
    url(r'^courses/(?P<id>\d+)/comments/show$', views.show),
    url(r'^courses/(?P<id>\d+)/comments/create$', views.createcomment)
]