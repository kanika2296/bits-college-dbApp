from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.home,name="Home"),
    path('updatescore/',views.updatescore,name="updatescore"),
    url(r'^teacher/(?P<id>\d+)/$', views.teacher, name='teacher'),
    url(r'^teachers/(?P<id>\d+)/(?P<id1>\d+)/$', views.teacher, name='teachers'),
    url(r'^student/(?P<id>\d+)/$', views.student, name='student'),
    url(r'^students/(?P<id>\d+)/(?P<id1>\d+)/$', views.student, name='students'),
    url(r'^ta/(?P<id>\d+)/$', views.ta, name='ta'),
    url(r'^tas/(?P<id>\d+)/(?P<id1>\d+)/$', views.ta, name='tas'),
]
