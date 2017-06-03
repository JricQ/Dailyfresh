#coding:utf-8
from django.shortcuts import render
from django.http import JsonResponse
from models import *

# Create your views here.
def index(request):
	t1_click = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:3]
	t1_new = GoodsInfo.objects.filter(gtype_id=1).order_by('-gclick')[0:4]
	# 上面两个不懂

	context = {
		'title':'首页',
		't1_click':t1_click,
		't1_new': t1_new,
	}

	return render(request, 'app_goods/index.html', context)

def index2(request, tid):
	# 查询点击量最高, 最新的商品
	t1_click = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')[0:3]
	t1_new = GoodsInfo.objects.filter(gtype_id=int(tid)).order_id('id')[0:4]
	# 构造点击量最高的商品列表
	click_list=[]
	for click in ti_click:
		click_list.append({'id':click.id, 'title':click.click.gtitle_id})
	# 构造最新的商品列表
	new_list = []
	for new in t1_new:
		new_list.append({'id':new.id,'title':new.gtitle_id,'price':new.gprice,'pic':new.gpic.name})
		context={'click_list':click_list,'new_list':new_list}
		return JsonResponse(context)