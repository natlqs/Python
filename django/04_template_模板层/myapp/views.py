from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from datetime import datetime
from myapp.models import Cities

# Create your views here.
def index(request):
    return render(request, "myapp/index.html")


def demo1(request):
    '''模板的语法'''
    context = {}
    context['name'] = 'ZhangSan'
    context['a'] = [10, 20, 30]
    context['stu'] = {'name': 'lisi', 'age':20}
    data = [
        {"name":'张翠山', 'sex':1, 'age':40, 'state':0},
        {"name":'殷素素', 'sex':0, 'age':38, 'state':2},
        {"name":'张无忌', 'sex':1, 'age':20, 'state':1},
        {"name":'赵敏', 'sex':0, 'age':18, 'state':2},
    ]
    context['dlist'] = data
    context['time'] = datetime.now
    context['m1'] = 100
    context['m2'] = 20
    return render(request, 'myapp/demo1.html', context)

def demo2(request):
    '''模板继承'''
    return render(request, 'myapp/demo2.html')

# 加载城市级联信息操作模板
def showcity(request):
    return render(request, "myapp/city.html")

# 加载对应的城市信息函数，返回json数据格式
def cities(request, upid=0):
    citylist = Cities.objects.filter(provinceCode=upid)
    citieslist = []
    for ob in citylist:
        citieslist.append({"code":ob.code, "name":ob.name, "provinceCode":ob.provinceCode})
    return JsonResponse({"data":citieslist})
  

