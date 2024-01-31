from django.http import HttpResponse
from django.shortcuts import render

# 移动端首页
def index(request):
    return HttpResponse("欢迎进入移动会员端首页！")