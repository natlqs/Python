from nicegui import ui
from ex4nicegui import to_ref, ref_computed, effect, effect_refreshable

# 容器 column
with ui.column():
    ui.button('Refresh')
    ui.button("button2")
    ui.button("button3")


# 容器 row
with ui.row():
    ui.label("box1")
    ui.label("box2")
    ui.label("box3")

# 容器 grid
with ui.grid():
    ui.label("box1")
    ui.label("box2")
    ui.label("box3")

ui.run()