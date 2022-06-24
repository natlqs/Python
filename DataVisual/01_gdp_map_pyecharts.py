import pandas as pd
from pyecharts.charts import Map
from pyecharts import options as opts
from pyecharts.globals import ThemeType  # 引入主题

data = pd.read_excel(r'./DataVisual/gdp.xlsx')  # 读取表格
province = list(data['province'])
gdp = list(data['2019gdp'])
list = [list(z) for z in zip(province, gdp)]
# print(list)

c = (
    Map(init_opts=opts.InitOpts(width='1900px',
                                height='1000px',
                                theme=ThemeType.LIGHT))  # 初始化地图大小
    .set_global_opts(
        title_opts=opts.TitleOpts(title='2019年各省GDP分布图    单位：亿元'),  # 配置标题
        visualmap_opts=opts.VisualMapOpts(
            min_=1000,
            max_=110000,
            range_text=['GDP总量（亿）颜色区间：', ''],  # 分区间
            is_piecewise=True,  # 定义图例为分段型， 默认为连续的图例
            pos_top='middle',  # 分段位置
            pos_left='left',
            orient='vertical',
            split_number=20  # 分成10个区间
            # type_='scatter'
        )).add('GDP', list, maptype='china')  # 将list传入，地图类型为中国地图
    .render(r"./DataVisual/map2.html"))
