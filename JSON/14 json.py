# 从populations.json取每个名称信息，然后将每一个名称放入getCountryCode( )方法中找寻相关代码，如果找到则输出相对应的代码，如果找不到则输出“名称不吻合”。
import json
from pygal.maps.world import COUNTRIES


def getCountryCode(countryName):
    '''输入名称回传代码'''
    for dictCode, dictName in COUNTRIES.items():    # 搜寻代码字典
        if dictName == countryName:
            return dictCode             # 如果找到就回传代码
    return None         

fn = '.\\python\\JSON\\population_data.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)     # 读取入门数据json文件

for getData in getDatas:
    if getData['Year'] == '2000':
        countryName = getData['Country Name']
        countryCode = getCountryCode(countryName)
        population = int(float(getData['Value']))
        if countryCode != None:
            print(countryCode, ':', population)
        else:
            print(countryName, '名称不符合')