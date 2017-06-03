#coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def login(self):
	def login_fun(request, *args, **kwargs):
		if request.session.has_key('user_id'):
			return func(request, *args, **kwargs)
		else:
			red = HttpResponseRedirect('/users/login/')
			red.set_cookie('url',request.get_full_path())
			return red