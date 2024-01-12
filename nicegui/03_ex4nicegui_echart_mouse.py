from nicegui import ui
from ex4nicegui.reactive import rxui

opts = {
    "xAxis": {"type":"value", "boundaryGap":[0, 0.01]},
    "yAxis": {
        "type":"category",
        "data":["Brazil", "Indonesia", "USA", "India", "China", "World"],
    },
    "series": [
        {
            "name": "first",
            "type":"bar",
            "data":[18203, 23489, 29034, 104970, 131744, 630230],
        },
        {
            "name": "second",
            "type":"bar",
            "data":[19325, 23438, 31000, 121594, 134141, 681807],
        },
    ],
}

bar = rxui.echarts(opts)

def on_click(e: rxui.echarts.EChartsMouseEventArguments):
    ui.notify(f"on_click:{e.seriesName}:{e.name}:{e.value}")

def on_first_series_mouseover(e: rxui.echarts.EChartsMouseEventArguments):
    ui.notify(f"on_first_series_mouseover:{e.seriesName}:{e.name}:{e.value}")

bar.on("click", on_click)
bar.on("mouseover", on_first_series_mouseover, query={"seriesName": "first"})
ui.run()