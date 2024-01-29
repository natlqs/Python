from django.db import models
from datetime import datetime

# 创建完模型后要先执行： python manage.py makemigrations
# 然后执行： python manage.py migrate


# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)     # 主键可省略不写
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=20)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)

# class Meta:
    # db_table = 'myapp_users'   # 指定表名可省略不写