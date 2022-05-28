# 程序执行时会要求输入账号，然后列出所输入账号同时打印欢迎使用本系统。

import json
fn = '.\\python\\JSON\\login.json'
login = input('请输入账号:')
with open(fn, 'w') as fnObj:
    json.dump(login, fnObj)
    print('%s! 欢迎使用本系统' % login)