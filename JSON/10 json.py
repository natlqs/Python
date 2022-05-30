# 读取login.json的数据，同时输出'欢迎回来使用本系统'

import json

fn = '.\\python\\JSON\\login.json'
with open(fn, 'r') as fnObj:
    login = json.load(fnObj)
    print('%s 欢迎回来使用本系统！' % login)
