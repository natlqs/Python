# 列出population_data.json数据中的人口数据
import json
fn = '.\\python\\JSON\\population_data.json'
with open(fn) as fnObj:
    getDatas = json.load(fnObj)

for getData in getDatas:
    if getData['Year'] == '2000':
        countryName = getData['Country Name']
        countryCode = getData['Country Code']
        population = int(float(getData['Value']))
        print('代码 = ', countryCode)
        print('名称 = ', countryName)
        print('人口数= ', population)
