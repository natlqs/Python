from nicegui import ui, ui_run  # 从nicegui库中导入ui和ui_run函数
from ex4nicegui.reactive import rxui  # 从ex4nicegui.reactive库中导入rxui函数
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable  # 从ex4nicegui库中导入to_ref、ref_computed、effect和effect_refreshable函数

# 定义一个引用，初始值为10
r_num = to_ref(10)

# 创建一个滑动条组件，将r_num引用作为滑动条的值
rxui.slider(1, 100, value=r_num)

# 定义一个函数，当滑动条的值发生变化时，该函数将被调用
@effect_refreshable
def _():
   # 创建一个标签组件，显示当前的滑动条值
   ui.label(str(r_num.value))

# 运行应用程序
ui_run()
