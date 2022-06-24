import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType

data = pd.read_excel('./DataVisual/gdp.xlsx')
province = list(data['province'])
gdp = list(data['2019gdp'])
list = [list(z) for z in zip(province, gdp)]
# print(list)
d = (
    Geo().add_schema(maptype='china').add(
        'geo',
        list,  # 传入数据
        symbol_size=10,
        large_threshold=110000,  # 设置涟漪大小
        type_=ChartType.EFFECT_SCATTER,  # 地图类型为涟漪图
    ).set_series_opts(label_opts=opts.LabelOpts(
        is_show=False)).set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=110000),
            title_opts=opts.TitleOpts(
                title='2019年各省GDP涟漪图')).render(r'./DataVisual/Geomap1.html'))
