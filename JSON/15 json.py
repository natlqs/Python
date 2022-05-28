import json 
from pygal_maps_world.i18n import COUNTRIES
import pygal.maps.world

fn = '.\\python\\JSON\\population_data.json'

with open(fn) as fnObj:
    getDatas = json.load(fnObj)

def get_country_code(country_name):
    '''
    pygal中的地图制作工具要求数据为特定的格式：用国别码表示国家，以及用数字表示人口数量
    因为pygal使用两个字母的国别码，所以我们要想办法过呢据国家名称获取两个字母的国别码
    '''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

# 打印人口数量
ccPopulations = {}
for getData in getDatas:
    if getData['Year'] == '2000':
        countryName = getData['Country Name']
        population = getData['Value']
        population = int(float(population))     # 将数值转换为整数
        code = get_country_code(countryName)
        if code:
            print(code + ':' + str(population))
            ccPopulations[code] = population
        else:
            print('Error- ' + countryName)

# 制作颜色的地图    
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
'''
方法add()接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码
每次调用add()都将为指定的国家选择一种新的颜色，并在图标左边显示该颜色和指定的标签
'''
wm.add('North America', ['ca', 'mx', 'us'])     
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('.\\python\\JSON\\americas.svg')      # 制作地图



# 绘制完整的世界人口地图
wm = pygal.maps.world.World()
wm.title = 'World Population in 2000, by Country'
wm.add('2000', ccPopulations)
wm.render_to_file('.\\python\\JSON\\World_Population.svg')      # 世界人口地图
print(ccPopulations)