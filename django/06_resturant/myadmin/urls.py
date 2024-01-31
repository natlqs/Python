
from django.urls import path
from myadmin.views import index

urlpatterns = [
    # 后台首页
    path("", index.index, name="myadmin_index"),
]
