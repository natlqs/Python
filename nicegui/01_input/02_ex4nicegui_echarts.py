from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import ref_computed, effect, to_ref

r_input = to_ref('')

# ref_computed 创建只读响应式变量
# 函数中使用任意其他响应式变量，会自动关联
@ref_computed
def cp_echarts_opts():
    return{
        "title":{"text": r_input.value}, # 字典中使用任意响应式变量，通过.value获取值
        "xAxis":{
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type":"value"},
        "series":[
            {
                "data":[120, 200, 150, 80, 70, 110, 130,],
                "type":"bar", 
                "showBackground":True,
                "backgroundStyle":{"color":"rgba(180, 180, 180, 0.2)"},
            }
        ]
    }

input = rxui.input("输入内容，图表标题会自动同步", value=r_input)

# 通过响应式组件对象的element属性，获取原生nicegui组件对象
input.element.classes("w_full")

rxui.echarts(cp_echarts_opts)
ui.run()