from django.conf.urls import patterns, url

from myApp import views

#from blogapp.myApp.api import Post
urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),

    url(r'^(?P<post_id>\d+)/$', views.blogShow, name='post'),
)
