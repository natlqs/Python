from nicegui import ui
from ex4nicegui.reactive import rxui
import viewData
from ex4nicegui import effect_refreshable


def build():
    # 添加一个分割线
    ui.separator()

    # 使用 rxui.expansion 创建一个可展开的Card，标题为 "图表"，并将其绑定到 viewData.can_load_data 引用的对象
    with rxui.expansion("图表").classes("w-full").bind_visible(viewData.can_load_data):
        # 使用 rxui.select 创建一个下拉选择框组件，用于选择数据中的统计列
        rxui.select(
            viewData.data_str_cols,  # 选项来自 viewData.data_str_cols 引用的对象
            label="一级统计列",  # 标签为 "一级统计列"
            value=viewData.r_group_level_1_select,  # 初始值为 viewData.r_group_level_1_select
            clearable=True,  # 可清除选择
        )
        # 使用 rxui.select 创建一个下拉选择框组件，用于选择数据中的统计列
        rxui.select(
            viewData.data_str_cols,  # 选项来自 viewData.data_str_cols 引用的对象
            label="二级统计列",  # 标签为 "二级统计列"
            value=viewData.r_group_level_2_select,  # 初始值为 viewData.r_group_level_2_select
            clearable=True,  # 可清除选择
        )
        # 使用 rxui.select 创建一个下拉选择框组件，用于选择数据中的统计指标列
        rxui.select(
            viewData.data_number_cols,  # 选项来自 viewData.data_number_cols 引用的对象
            label="统计指标列",  # 标签为 "统计指标列"
            value=viewData.r_group_value_col_select,  # 初始值为 viewData.r_group_value_col_select
            clearable=True,  # 可清除选择
        )

        with ui.card():
            ui.markdown(
                """## 说明
               - 此图标配置来源echarts官网
               - 选择二级统计列后，可点击下方图标系列，二级统计图表会联动变化"""
            )

        with ui.grid(columns=2).classes("w-full"):
            with rxui.card().bind_visible(viewData.can_level1_chart_show):
                ui.link(
                    "点击打开echarts饼图自定义样式",
                    "https://echarts.apache.org/examples/zh/editor.html?c=pie-custom",
                    new_tab=True,
                )
                pie = rxui.echarts(viewData.level1_chart_data).classes(
                    "h-[50vh] w-full"
                )

            viewData.bind_click_ref(pie)
        
            with rxui.card().bind_visible(viewData.can_level2_chart_show):
                ui.link(
                    "点击打开pyecharts饼图自定义样式",
                    "https://gallery.pyecharts.org/#/Bar/bar_markline_type",
                    new_tab=True,
                )

                @effect_refreshable
                def _():
                    if viewData.can_level2_chart_show.value:
                        rxui.echarts.from_pyecharts(viewData.level2_chart_data).classes(
                            "h-[50vh] w-full"
                        )