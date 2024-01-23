from django.urls import path, include
from myapp import views
from myapp.views import MyView


urlpatterns = [
    path('', views.index, name="index"), # 首页
    path("resp01", views.resp01, name="response01"),    # 一个简单的视图
    path("resp02", views.resp02, name="response02"),    # 返回一个错误
    path("resp03", views.resp03, name="response03"),    # 重定向
    path("resp04", MyView.as_view(), name="response04"),    # 基于类的视图
    path("resp05", views.resp05, name="response05"),    # Json响应
    path("resp06", views.resp06, name="response06"),    # Cookie的使用
    path("resp07", views.resp07, name="response07"),    # 测试request请求对象的使用
    path("resp08", views.verifycode, name="response08"),    # 验证码的输出

]