#myapp应用中的自定义二级路由配置
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 模板语法测试路由
    path('demo1', views.demo1, name='demo1'),
    # 模板继承测试路由
    path('demo2', views.demo2, name='demo2'),

]