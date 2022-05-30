import imp
import json 
from pygal_maps_world.i18n import COUNTRIES
import pygal.maps.world
from pygal.style import RotateStyle, LightColorizedStyle

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

#当前地图中，很多国家都是浅色的，只有两个国家是深色的。对大多数国家而言，颜色深浅差别不足以反映其人口数量的差别。
#为修复这种问题，我们将根据人口数量将国家分组，再分别对每个组着色：
ccPopulations1 , ccPopulations2, ccPopulations3 = {}, {}, {}
for countrynames, populations in ccPopulations.items():
    if populations< 10000000:
        ccPopulations1[countrynames] = populations
    elif populations < 100000000:
        ccPopulations2[countrynames] = populations
    else:
        ccPopulations3[countrynames] = populations

print(len(ccPopulations1), len(ccPopulations2), len(ccPopulations3))
wm_style = RotateStyle('#336688', base_style=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title='World Population in 2000, by Country'
wm.add('0-10m', ccPopulations1)
wm.add('10m-1bn', ccPopulations2)
wm.add('1b-10bn', ccPopulations3)
wm.render_to_file('.\\python\\JSON\\World_pupulation_2000.svg')


# # 制作颜色的地图
# wm = pygal.maps.world.World()
# wm.title = 'North, Central, and South America'
# '''
# 方法add()接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码
# 每次调用add()都将为指定的国家选择一种新的颜色，并在图标左边显示该颜色和指定的标签
# '''
# wm.add('North America', ['ca', 'mx', 'us'])     
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
#     'gy', 'pe', 'py', 'sr', 'uy', 've'])
# wm.render_to_file('.\\python\\JSON\\americas.svg')      # 制作地图



# # 绘制完整的世界人口地图
# wm = pygal.maps.world.World()
# wm.title = 'World Population in 2000, by Country'
# wm.add('2000', ccPopulations)
# wm.render_to_file('.\\python\\JSON\\World_Population.svg')      # 世界人口地图
# print(ccPopulations)
