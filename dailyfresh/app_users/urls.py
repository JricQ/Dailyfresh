#coding=utf-8

from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^login/$', views.login),
	url(r'^register/$', views.register),
	url(r'^register_list/$', views.register_list),
	url(r'^register_exist/$', views.register_exist),
	url(r'^login_handle/$', views.login_handle),
	url(r'^logot/$', views.logout),
	url(r'^info/$', views.info),
	url(r'^order/$', views.order),
	url(r'^site/$', views.site),
]