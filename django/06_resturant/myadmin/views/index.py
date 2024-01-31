from django.shortcuts import render
from django.http import HttpResponse

# 后台首页
def index(request):
    return render(request, "myadmin/index/index.html")