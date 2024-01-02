from nicegui import ui, ui_run
from ex4nicegui.reactive import rxui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable


r_num = to_ref(10)
rxui.slider(1, 100, value=r_num)

@effect_refreshable
def _():
    # for num in range(r_num.value):
        ui.label(str(r_num.value))


ui.run()
   