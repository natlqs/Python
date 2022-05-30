# 第一次登录会要求输入账号然后将输入账号记录在login24_10.json文件内，如果不是第一次登录，会直接读取已经存在login24_10.json的账号，然后打印“欢迎回来”。
import json

fn = '.\\python\\JSON\\repeatlogin.json'

try:
    with open(fn) as fnObj:
        login = json.load(fnObj)
except Exception:
    login = input('请输入账号: ')
    with open(fn, 'w') as fnObj:
        json.dump(login, fnObj)
        print('系统已记录你的账号')
else:
    print("%s 欢迎回来" % login)