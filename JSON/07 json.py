# 将一个字典数据，使用json格式存储在07jsonout.json文件内，在这个实例中，dump()方法的第一个参数
# 是欲存储成json格式的数据，第二个参数是欲存储的文件对象

import json

dictObj = {'b':80, 'a':25, 'c':60}
fn = '.\\python\\JSON\\07jsonout.json'
with open(fn, 'w') as fnObj:
    json.dump(dictObj, fnObj)