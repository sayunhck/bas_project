#coding=utf-8
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
#渲染登录首页
def index_view(request):
    return render(request,'login.html')

#处理登录功能
def login_view(request):
    #接收表单请求参数
    uname = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')
    #判断
    if uname=='tt_hlj_haochenkai' and pwd=='123':
        return HttpResponse('登录成功！！！！')

    return HttpResponse('登录失败！')