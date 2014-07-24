#references:
#
#!/usr/bin/python
#coding:utf8

__author__ = ['leo.adams']


from django.conf.urls import patterns, url
from user import views

urlpatterns = patterns('',
        url(r'^$',views.index,name='index'),
        url(r'^(?P<user_id>\d+)/$',views.detail, name= 'detail'),
        url(r'^(?P<user_id>\d+)/clock/$',views.clock, name= 'clock'),
        url(r'^(?P<user_id>\d+)/results/$',views.results, name= 'results'),
        )
