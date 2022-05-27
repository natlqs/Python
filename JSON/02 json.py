# 将python由字典元素所组成的列表转成json数组，转换后原先字典元素变为json的对象

import json
listObj = [{'Name':'Peter', 'Age':25, 'Gender':'M'}]        # 列表数据元素是字典
jsonData = json.dumps(listObj)              # 将列表数据转成json数据
print('列表转成json的数组', jsonData)
print('json数组在python的数据类型', type(jsonData))