from django.db import models

# Create your models here.
class Cities(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    provinceCode = models.IntegerField()

class Meta:
    db_table="city"     # 指定真实表名
