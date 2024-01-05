from nicegui import ui

@ui.page('/funcA')
def funcA():
    ui.label("function A").props('style="font-size: 5rem"')
    with ui.row():
        ui.icon('B', color = 'orange', size="4rem")
        ui.link("跳转到页面B", "/funcB").props('style="font-size:3rem"')
    with ui.row():
        ui.icon('home', color = 'green', size="3rem")
        ui.link("跳回到主页面", "/").props('style="font-size:3rem"')

    input = ui.input("传递到C页面的内容")
    def onclick():
        ui.open(f'/funcC/{input.value}')
    ui.button("打开页面C", on_click=onclick)

@ui.page('/funcB')
def funcB():
    ui.label("function B").props('style="font-size: 5rem"')
    with ui.row():
        ui.icon('A', color = 'orange', size="4rem")
        ui.link("跳转到页面A", "/funcA").props('style="font-size:3rem"')
    with ui.row():
        ui.icon('home', color = 'green', size="3rem")
        ui.link("跳回到主页面", "/").props('style="font-size:3rem"')

    input = ui.input("传递到C页面的内容")
    def onclick():
        ui.open(f'/funcC/{input.value}')
    ui.button("打开页面C", on_click=onclick)

@ui.page('/funcC/{text}')
def funcC(text: str):
    ui.label("function C").props('style="font-size: 5rem"')
    ui.label(f"接收到的内容是：{text}").props('style="font-size: 3rem"')
    with ui.row():
        ui.icon('A', color = 'orange', size="4rem")
        ui.link("跳转到页面A", "/funcA").props('style="font-size:3rem"')
    with ui.row():
        ui.icon('B', color = 'orange', size="4rem")
        ui.link("跳转到页面B", "/funcB").props('style="font-size:3rem"')
    with ui.row():
        ui.icon('home', color = 'green', size="3rem")
        ui.link("跳回到主页面", "/").props('style="font-size:3rem"')


with ui.row():
    ui.icon('home', color = 'green', size= "4rem")
    ui.label("main page").props('style="font-size: 3rem"')
with ui.row():
    ui.icon('A', color = 'orange', size= "4rem")
    ui.link("跳转到页面A", "/funcA").props('style="font-size: 3rem"')
with ui.row():
    ui.icon('B', color = 'orange', size="4rem")
    ui.link("跳转到页面B", "/funcB").props('style="font-size: 3rem"')
# with ui.row():
#     ui.icon('C', color = 'orange', size="4rem")
#     ui.link("跳转到页面B", "/funcC").props('style="font-size: 3rem"')


ui.run()
