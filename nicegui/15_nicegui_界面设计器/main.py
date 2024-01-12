from nicegui import ui
from niceguiToolkit.layout import inject_layout_tool

inject_layout_tool()
with ui.card() , ui.row():
    ui.avatar("home").style("font-size:4.8rem;color:#ff0000")
    with ui.column():
        with ui.row().style("font-size:1.0rem"):
                ui.label("数据大宇宙")
                ui.icon("mail")
                ui.label("发消息")

        with ui.row().style("color:#ff0000;flex-direction:row;gap:1.3rem"):
                ui.button("充电")
                ui.button("+ 关注 670")

ui.run()