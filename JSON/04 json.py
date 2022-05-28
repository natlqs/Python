# 将字典转成json格式的对象，分别是未使用排序与使用排序。
import json
from pstats import SortKey
dicObj = {'b':88, 'a':25, 'c':165}
jsonObj1 = json.dumps(dicObj)
jsonObj2 = json.dumps(dicObj, sort_keys= True)
print('未用排序将字典转换成json对象', jsonObj1)
print('使用排序将字典转换成json对象', jsonObj2)
print('有排序与未排序对象是否相同', jsonObj1 == jsonObj2)
print('json物件在python的数据类型', type(jsonObj1))