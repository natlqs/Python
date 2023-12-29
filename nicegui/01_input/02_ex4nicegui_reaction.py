from nicegui import ui
from ex4nicegui import ref_computed, effect, to_ref
from ex4nicegui.reactive import rxui

# 定义响应式数据
r_input = to_ref("aaa")

# 按照 nicegui使用方式传入响应式数据即可
rxui.input(value=r_input)
rxui.label(r_input)


ui.run()

