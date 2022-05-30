# 读取json文件07jsonout.json，同时列出结果
import json

fn = '.\\python\\JSON\\07jsonout.json'
with open(fn, 'r') as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))