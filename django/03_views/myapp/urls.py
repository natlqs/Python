from django.urls import path, include
from myapp import views


urlpatterns = [
    path('', views.index, name="index"), # 首页
    path("resp01", views.resp01, name="response01"),
    path("resp02", views.resp02, name="response02"),
]