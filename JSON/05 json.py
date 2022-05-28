# 将python的字典转成json格式对象时，设定缩排4个字符宽度。
import json
dicObj = {'b':80, 'a':25, 'c':80 }
jsonObj = json.dumps(dicObj, sort_keys=True, indent=4)      # 用内缩呈现json对象
print(jsonObj)