from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable
from icons import ICON_NAMES

r_input = to_ref("")  # 定义一个名为 r_input 的变量，并将其初始化为空字符串


# 创建响应式计算
@ref_computed  # 使用 @ref_computed 装饰器定义一个响应式计算函数
def cp_icon_names():  # 定义一个名为 cp_icon_names 的函数，用于计算分页数据
    return [
        name for name in ICON_NAMES if name.find(r_input.value) >= 0
    ]  # 返回一个包含匹配输入内容的 ICON_NAMES 列表


# 创建分页对象
r_pagination = rxui.use_pagination(
    cp_icon_names, page_size=80
)  # 使用 rxui.use_pagination 函数创建一个分页对象，传入分页数据和每页显示的项目数


# 创建分页对象
r_pagination = rxui.use_pagination(cp_icon_names, page_size=80)

# endregion

# region  界面
# 创建输入框组件， 设置基本功能，包含边框、输入延迟半秒等
input_search = (  # 定义一个名为 input_search 的变量
    rxui.input(  # 创建一个名为 input_search 的输入框组件
        "icon搜索",  # 为输入框设置一个描述信息，即 "icon搜索"
        value=r_input,  # 为输入框设置一个初始值，即 r_input
        placeholder="请输入搜索icon内容",  # 为输入框设置一个提示信息，即 "请输入搜索icon内容"
    )
    .props(
        'outlined clearable debounece = "500"'
    )  # 为输入框添加一些属性，包括 "outlined"（是否为圆角边框）、"clearable"（是否可清除内容）和 "debounece = '500'"（延迟触发输入事件，单位为毫秒）
    .classes(
        "self-center w-[20rem]"
    )  # 为输入框添加一些样式类，包括 "self-center"（水平居中）和 "w-[20rem]"（宽度为 20rem）
)


# 把函数的 图标单独做展示
def icon_box(icon_name: str):  # 定义一个名为 icon_box 的函数，用于创建一个包含图标和标签的卡片组件
   with ui.card().classes(  # 使用 with 语句创建一个卡片组件，并设置一些样式类
       "flex-center cursor-pointer gap-1 transition-all hover:scale-105 hover:text-blue-500"
   ) as card:  # 将 card 变量绑定到创建的卡片组件
       ui.icon(icon_name, size="3rem")  # 创建一个名为 icon 的图标组件，并设置其大小为 3rem
       ui.label(icon_name).classes(  # 创建一个名为 label 的标签组件，并设置一些样式类
           "whitespace-nowrap overflow-hidden text-ellipsis max-w-full"
       )

       # 鼠标经过时会显示提示框
       ui.tooltip(f"点击复制名字[{icon_name}]")  # 创建一个名为 tooltip 的提示框组件，并设置提示内容为 "点击复制名字[{icon_name}]"

   def on_click_copy_icon_name():  # 定义一个名为 on_click_copy_icon_name 的异步函数，用于处理点击图标的事件
       ui.run_javascript(  # 使用 await 关键字调用 ui.run_javascript 函数
           f'navigator.clipboard.writeText("{icon_name}")'  # 传入一个 JavaScript 代码字符串，用于将 icon_name 写入剪贴板
       )

       ui.notify(f"已复制名字[{icon_name}]到剪贴板", position="top-right")  # 创建一个名为 notify 的通知组件，并设置通知内容为 "已复制名字[{icon_name}]到剪贴板"

   card.on("click", on_click_copy_icon_name)  # 将 on_click_copy_icon_name 函数绑定到 card 组件的点击事件



## 小图标展示区
with ui.grid(columns=10).classes("w-full"):  # 使用 with 语句创建一个网格组件，并设置一些样式类

    @effect_refreshable  # 使用 effect_refreshable 装饰器创建一个动态刷新的函数
    def _():  # 定义一个名为 _ 的函数，用于创建一个包含图标和标签的卡片组件
        for icon_name in r_pagination.current_source.value:  # 遍历当前分页的数据
            icon_box(icon_name)  # 调用 icon_box 函数，传入 icon_name 参数


# 通过分页对象创建分页组件
r_pagination.create_q_pagination()  # 调用 r_pagination 对象的 create_q_pagination 方法，创建一个分页组件


# endregion

ui.run()
