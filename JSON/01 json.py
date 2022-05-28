# 将python的列表与元组数据转成json的数组数据的实例
import json
listNumbers = [5, 10, 20, 1]        # 列表数据
tupleNumbers = (1, 5, 10, 9)        # 元组资料
jsonData1 = json.dumps(listNumbers)     # 将列表数据转成json数据
jsonData2 = json.dumps(tupleNumbers)        # 将列表数据转成json数据
print('列表转成json的数组', jsonData1)
print('元组转成json的数组', jsonData2)
print('json数组在python的数据类型', type(jsonData1))