# This script imports necessary libraries and defines reactive variables for the NiceGUI app
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, on
import openpyxl
import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Bar, Line

# 定义反应式引用变量
r_current_file = to_ref(r"")  # 定义当前文件路径的引用变量
r_current_sheet = to_ref("")  # 定义当前工作表名称的引用变量
r_file_changed = to_ref(None)  # 定义文件更改标志的引用变量

r_group_level_1_select = to_ref("")  # 定义第一级分组列选择器的引用变量
r_group_level_2_select = to_ref("")  # 定义第二级分组列选择器的引用变量
r_group_value_col_select = to_ref("")  # 定义值列选择器的引用变量

# 点击第一级图标的系列名
r_chart_level1_click_series_name = to_ref("")

# 定义绑定第一级图表点击事件的方法
def bind_click_ref(chart_level1: rxui.echarts):
   @effect
   def _():
       click_ref = chart_level1.click_info_ref
       if click_ref.value is not None:
           r_chart_level1_click_series_name.value = click_ref.value.name

   @chart_level1.element.on_click_blank
   def _(e):
       r_chart_level1_click_series_name.value = ""

# 定义重置当前工作表的方法
@on(r_current_file)
def reset_current_sheet():
   r_current_sheet.value = ""

# 定义重置所有选择器值的方法
@on(r_current_sheet)
def reset_all_select():
   r_group_level_1_select.value = ""
   r_group_level_2_select.value = ""
   r_group_value_col_select.value = ""
   r_chart_level1_click_series_name.value = ""

# 定义第一级分组列选择器值改变时清空图表点击列的方法
@on(r_group_level_1_select)
def reset_chart_click_when_level1_select_changed():
   """当第一级分组列改变时，清空图表点击列"""
   r_chart_level1_click_series_name.value = ""


# region 计算属性


@ref_computed
def sheet_names():
    if not r_current_file.value:
        return []

    workbook = openpyxl.load_workbook(r_current_file.value)
    sheet_names = workbook.sheetnames
    return sheet_names


@ref_computed
def can_load_data():
    return bool(r_current_file.value) and bool(r_current_sheet.value)


@ref_computed
def data():
    if not can_load_data.value:
        return pd.DataFrame({})

    r_file_changed.value
    return pd.read_excel(r_current_file.value, sheet_name=r_current_sheet.value)


@ref_computed
def data_str_cols():
    if not can_load_data.value:
        return []

    return data.value.select_dtypes("object").columns.tolist()


@ref_computed
def data_number_cols():
    if not can_load_data.value:
        return []

    return data.value.select_dtypes("number").columns.tolist()


@ref_computed
def can_level1_chart_show():
    """第一级汇总的图表是否显示"""
    return (
        can_load_data.value
        and bool(r_group_level_1_select.value)
        and bool(r_group_value_col_select.value)
    )


@ref_computed
def can_level2_chart_show():
    """第二级汇总的图表是否显示"""
    return (
        can_load_data.value
        and bool(r_group_level_2_select.value)
        and bool(r_group_value_col_select.value)
    )


@ref_computed
def level1_chart_data():
    """一级图表数据源"""
    if not can_level1_chart_show.value:
        return {}

    level_1_col = r_group_level_1_select.value
    value_col = r_group_value_col_select.value

    title = f"统计 [{level_1_col}] {value_col} 指标"

    gp_data = (
        data.value.groupby(level_1_col)
        .agg({value_col: "sum"})
        .reset_index()
        .rename(
            columns={
                level_1_col: "name",
                value_col: "value",
            }
        )
    )

    visualMap_min = gp_data["value"].min()
    visualMap_max = gp_data["value"].max()

    visualMap_min = visualMap_min * (1 - 0.4)
    visualMap_max = visualMap_max * (1 + 0.2)

    chart_data = gp_data.to_dict("records")

    return {
        "backgroundColor": "#2c343c",
        "title": {
            "text": title,
            "left": "center",
            "top": 20,
            "textStyle": {"color": "#ccc"},
        },
        "tooltip": {"trigger": "item"},
        "visualMap": {
            "show": False,
            "min": visualMap_min,
            "max": visualMap_max,
            "inRange": {"colorLightness": [0, 1]},
        },
        "series": [
            {
                "name": "Access From",
                "type": "pie",
                "radius": "55%",
                "center": ["50%", "50%"],
                "data": chart_data,
                "roseType": "radius",
                "label": {"color": "rgba(255, 255, 255, 0.3)"},
                "labelLine": {
                    "lineStyle": {"color": "rgba(255, 255, 255, 0.3)"},
                    "smooth": 0.2,
                    "length": 10,
                    "length2": 20,
                },
                "itemStyle": {
                    "color": "#c23531",
                    "shadowBlur": 200,
                    "shadowColor": "rgba(0, 0, 0, 0.5)",
                },
                "animationType": "scale",
                "animationEasing": "elasticOut",
            }
        ],
    }


@ref_computed
def level2_chart_data():
    """二级图表数据源"""
    if not can_level2_chart_show.value:
        return (
            Bar()
        )  # 这个地方语义很奇怪，主要是因为 ex4ng没有针对空的情况的处理，后续版本修复

    click_series_name = r_chart_level1_click_series_name.value
    df = data.value

    if click_series_name:
        cond = df[r_group_level_1_select.value] == click_series_name

        df = df[cond]

    gp_data = (
        df.groupby(r_group_level_2_select.value)
        .agg({r_group_value_col_select.value: "sum"})
        .reset_index()
        .rename(
            columns={
                r_group_level_2_select.value: "name",
                r_group_value_col_select.value: "value",
            }
        )
    )

    xAxis_data = gp_data["name"].tolist()
    series_data = gp_data["value"].tolist()

    c = (
        Bar()
        .add_xaxis(xAxis_data)
        .add_yaxis(click_series_name or "all", series_data)
        .set_global_opts(
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=f"一级列[{r_group_level_1_select.value}=={click_series_name or 'all'}]，指标:[{r_group_value_col_select.value}]"
            ),
        )
        .set_series_opts(
            label_opts=opts.LabelOpts(is_show=False),
            markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值"),
                    opts.MarkLineItem(type_="average", name="平均值"),
                ]
            ),
        )
    )

    return c


g_fw = None


@on(can_load_data)
def watch_file():
    global g_fw

    if can_load_data.value:
        if g_fw is not None:
            g_fw.stop()

        g_fw = rxui.FilesWatcher(r_current_file.value)

        @g_fw.on_FileChange
        def _(e):
            print(e)
            r_file_changed.value = None


# endregion
