from django.urls import path, re_path, include
from . import views
urlpatterns = [
    path("myapp/", views.home),
    path("", views.home, name="index"),
    path("add/", views.add, name="add"),
    path("find/", views.find),  # 不带参数
    path("find/<int:id>/", views.find),     # 带一个参数   id
    path("find/<int:id>/<str:name>/", views.find),      # 带两个参数   id,name
    path("update/", views.update),
    path("edit/", views.edit),
    path("delete/", views.delete),
    path("jump", views.jump),
    path("databases", views.databases),

    # 正则表达式匹配
    re_path(r'^fun/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.fun),  # 带两个参数   id,name


    # 模型层测试， 配置Users操作数据路由

    path("")
]