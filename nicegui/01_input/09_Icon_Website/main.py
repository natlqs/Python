from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable
from icons import  ICON_NAMES

#region 数据
r_input = to_ref("")

# 创建响应式计算
@ref_computed
def cp_icon_names():
    return [name for name in ICON_NAMES if name.find(r_input.value) >= 0]

#endregion

#region  界面
# 创建输入框组件， 设置基本功能，包含边框、输入延迟半秒等
input_search = rxui.input(
    "icon搜索",
    value = r_input,
    placeholder="请输入搜索icon内容",
).props('outlined clearable debounece = "500"')

#temp
@ref_computed
def cp_date():
     return ",".join(cp_icon_names.value)

rxui.label(cp_date).classes("max-w-[50%] break-words")

#endregion

ui.run()