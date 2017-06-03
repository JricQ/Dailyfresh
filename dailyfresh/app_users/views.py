#coding=utf-8
from django.shortcuts import render, redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.

def login(request):
	return render(request, 'app_users/login.html')


def register(request):
	return render(request, 'app_users/register.html')
 
def register_list(request):
	# 接收用户输入
	post = request.POST
	uname = post.get('user_name')
	upwd = post.get('pwd')
	ucpwd = post.get('cpwd')
	uemail = post.get('email')
	# print 'upwd is %s'%upwd
	#判断两次密码是否一致:
	if upwd != ucpwd:
		return redirect('/register/')
	s1 = sha1()
	s1.update(upwd)
	upwd3 = s1.hexdigest()
	# print 'upwd3 is %s'%upwd3
	# 创建对象
	user = UsersInfo()
	user.users = uname
	user.upasswd = upwd3
	user.uemail = uemail
	user.save()
	# 注册成功, 返回登陆页面
	return redirect('/login/')

def register_exist(request):
	get_name = request.GET.get('uname')
	count = UsersInfo.objects.filter(users=get_name).count()
	print(count)
	return JsonResponse({'count':count})

def login_handle(request):
	# 接收post请求信息
	post = request.POST
	uname = post.get('username')
	upwd = post.get('pwd')
	memory = post.get('memory', 0)
	# 创建搜索对象,users是个列表
	users = UsersInfo.objects.filter(users=uname)

	print uname,upwd
	if len(users) == 1:
		s1 = sha1()
		s1.update(upwd)
		if s1.hexdigest() == users[0].upasswd:
			# 设置COOKIE
			# print '1'
			url = request.COOKIES.get('url','/')
			#重定向
			red = HttpResponseRedirect(url)
			#设置过期
			red.set_cookie('url','', max_age=-1)
			if memory!=0:
				red.set_cookie('users',uname)
			else:
				red.set_cookie('uname','',max_age=-1)
			request.session['user_id'] = users[0].id
			request.session['user_name']=uname
			return red
		else:
			# print'2'
			context = {'title': '用户登录','error_name': 0,'error_pwd': 1,'uname':uname,'upwd':upwd}
			return render(request,'app_users/login.html',context)
	else:
		context = {'title':'用户登录', 'error_name':1,'error_pwd': 0, 'uname':uname,'upwd':upwd}
		return render(request, 'app_users/login.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')


def info(request):

	return render(request, 'app_users/user_center_info.html')

def order(request):
	return render(request, 'app_users/user_center_order.html')

def site(request):
	return render(request, 'app_users/user_center_site.html')