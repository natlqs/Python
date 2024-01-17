"""
URL configuration for mydemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("myapp/", views.home),
    path("", views.home),
    path("add/", views.add),
    path("find/", views.find),  # 不带参数
    path("find/<int:id>/", views.find),     # 带一个参数   id
    path("find/<int:id>/<str:name>/", views.find),      # 带两个参数   id,name
    path("update/", views.update),
    path("edit/", views.edit),
    path("delete/", views.delete),

    # 正则表达式匹配
    re_path(r'^fun/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.fun),  # 带两个参数   id,name
]
