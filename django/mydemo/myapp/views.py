from django.shortcuts import render
from django.http import HttpResponse

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

# 正则表达式匹配
def fun(request, year, month):
    return HttpResponse(f"this is a regular pattern..., date is {year}, month is {month}")