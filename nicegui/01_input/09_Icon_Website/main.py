from nicegui import ui
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable


#region 数据
r_input = to_ref("")




#endregion


#region  界面
input_search = rxui.input(
    value = r_input,
)


#endregion



ui.run()