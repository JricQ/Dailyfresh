#coding=utf-8
from django.db import models



# Create your models here.
class UsersInfo(models.Model):
	# 用户名
	users = models.CharField(max_length=20)
	# 密码,使用sha1加密,要求40位
	upasswd = models.CharField(max_length=40)
	# 邮箱
	uemail = models.CharField(max_length=30)
	# 收件人姓名
	uname = models.CharField(max_length=20, default='')
	# 详细地址
	uaddr = models.CharField(max_length=100, default='')
	# 邮编
	upost = models.CharField(max_length=6, default='')
	# 手机 	 
	uphone = models.CharField(max_length=11, default='')

	class Meta:
		db_table = 'UsersInfo'