from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return HttpResponse("Hello, World!")
def add(request):
    return HttpResponse("adding...")
def find(request, id=0,name=''):
    return HttpResponse(f"finding...{id} results, and name is {name}")
def update(request):
    return HttpResponse("updating...")
def delete(request):
    return HttpResponse("deleting...")
def edit(request):
    return HttpResponse("editing...")
def jump(request):
    print(reverse("add"))   # reverse()函数可以通过路由名称反向解析出URL，这里返回URL的名称，
    # 然后通过这个名称可以跳转到相应的URL
    print(reverse("index"))
    # return HttpResponse("jumping...")
    return redirect("add")   # redirect()函数可以直接跳转到相应的URL

# 正则表达式匹配
def fun(request, year, month):
    return HttpResponse(f"this is a regular pattern..., date is {year}, month is {month}")