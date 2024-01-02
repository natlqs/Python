from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable

with ui.button('点击我'):
    ui.tooltip("提示我是按钮")
    with ui.menu().props("context-menu", remove="no-parent-event"):
        ui.menu_item('菜单项1')
        ui.menu_item('菜单项2')
        ui.menu_item('菜单项3')


ui.run()