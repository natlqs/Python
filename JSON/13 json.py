# 列出pygal.maps.world模块COUNTRIES字典的2个英文字母的地区代码与完整的地区名称列表
from pygal.maps.world import COUNTRIES

for countryCode in sorted(COUNTRIES.keys()):
    print('代码: ', countryCode, '名称', COUNTRIES[countryCode])
