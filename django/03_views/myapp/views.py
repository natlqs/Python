from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")

def resp01(request):
    return HttpResponse("<h3>一种简单的视图</h3>")
def resp02(request):
    return HttpResponseNotFound("<h3>ResponseNotFoud</h3>")