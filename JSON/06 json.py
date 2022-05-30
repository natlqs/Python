# 将json的对象数据转成python数据的实例，留意在建立json数据时，要加上引号，因为json数据在python内是以字符串形式存在
import json

jsonObj = '{"b":80, "a":25, "c":160}'
dicObj = json.loads(jsonObj)    # 转成python对象
print(dicObj)
print(type(dicObj))