from nicegui import ui


# 定义函数funcA，用于显示页面A的内容
@ui.page("/funcA")
def funcA():
    # 显示函数A的标题
    ui.label("function A").props('style="font-size: 5rem"')

    # 定义一个包含两个内容的行
    with ui.row():
        # 在第一个列中显示A图标，并设置其颜色、大小等样式
        ui.icon("B", color="orange", size="4rem")

        # 在第二个列中显示一个链接，链接到页面B，并设置其样式
        ui.link("跳转到页面B", "/funcB").props('style="font-size:3rem"')

    # 定义另一个包含两个内容的行
    with ui.row():
        # 在第一个列中显示home图标，并设置其颜色、大小等样式
        ui.icon("home", color="green", size="3rem")

        # 在第二个列中显示一个链接，链接到主页面，并设置其样式
        ui.link("跳回到主页面", "/").props('style="font-size:3rem"')

    # 定义一个输入框，用于接收传递到C页面的内容
    input = ui.input("传递到C页面的内容")

    # 定义一个按钮，用于打开页面C
    def onclick():
        # 打开页面C，并将传递到的内容作为参数传递
        ui.open(f"/funcC/{input.value}")

    # 显示一个按钮，用于打开页面C
    ui.button("打开页面C", on_click=onclick)


# 定义函数funcB，用于显示页面B的内容
@ui.page("/funcB")
def funcB():
    # 显示函数B的标题
    ui.label("function B").props('style="font-size: 5rem"')

    # 定义一个包含两个内容的行
    with ui.row():
        # 在第一个列中显示A图标，并设置其颜色、大小等样式
        ui.icon("A", color="orange", size="4rem")

        # 在第二个列中显示一个链接，链接到页面A，并设置其样式
        ui.link("跳转到页面A", "/funcA").props('style="font-size:3rem"')

    # 定义另一个包含两个内容的行
    with ui.row():
        # 在第一个列中显示home图标，并设置其颜色、大小等样式
        ui.icon("home", color="green", size="3rem")

        # 在第二个列中显示一个链接，链接到主页面，并设置其样式
        ui.link("跳回到主页面", "/").props('style="font-size:3rem"')

    # 定义一个输入框，用于接收传递到C页面的内容
    input = ui.input("传递到C页面的内容")

    # 定义一个按钮，用于打开页面C
    def onclick():
        # 打开页面C，并将传递到的内容作为参数传递
        ui.open(f"/funcC/{input.value}")

    # 显示一个按钮，用于打开页面C
    ui.button("打开页面C", on_click=onclick)


# 定义函数funcC，用于显示页面C的内容
# 定义函数 funcC，接收一个参数 text，类型为字符串
@ui.page('/funcC/{text}')
def funcC(text: str):
   # 在页面上添加一个标签，显示 "function C"
   ui.label("function C").props('style="font-size: 5rem"')
   # 在页面上添加一个标签，显示接收到的内容 text
   ui.label(f"接收到的内容是：{text}").props('style="font-size: 3rem"')
   # 创建一个行容器，包含两个列容器
   with ui.row():
       # 在第一个列容器中添加一个图标，内容为 A，颜色为橙色，大小为 4 rem
       ui.icon('A', color='orange', size="4rem")
       # 在第一个列容器中添加一个链接，内容为 "跳转到页面A"，跳转到 /funcA 页面
       ui.link("跳转到页面A", "/funcA").props('style="font-size:3rem"')
   # 在第二个列容器中添加一个图标，内容为 B，颜色为橙色，大小为 4 rem
   with ui.row():
       ui.icon('B', color='orange', size="4rem")
       # 在第二个列容器中添加一个链接，内容为 "跳转到页面B"，跳转到 /funcB 页面
       ui.link("跳转到页面B", "/funcB").props('style="font-size:3rem"')
   # 在第三个列容器中添加一个图标，内容为 home，颜色为绿色，大小为 3 rem
   with ui.row():
       ui.icon('home', color='green', size="3rem")
       # 在第三个列容器中添加一个链接，内容为 "跳回到主页面"，跳转到 / 页面
       ui.link("跳回到主页面", "/").props('style="font-size:3rem"')



# 创建一个行容器，包含两个列容器
with ui.row():
   # 在第一个列容器中添加一个图标，内容为 home，颜色为绿色，大小为 4 rem
   ui.icon('home', color='green', size="4rem")
   # 在第一个列容器中添加一个标签，显示 "main page"
   ui.label("main page").props('style="font-size: 3rem"')

# 创建一个行容器，包含两个列容器
with ui.row():
   # 在第一个列容器中添加一个图标，内容为 A，颜色为橙色，大小为 4 rem
   ui.icon('A', color='orange', size="4rem")
   # 在第一个列容器中添加一个链接，内容为 "跳转到页面A"，跳转到 /funcA 页面
   ui.link("跳转到页面A", "/funcA").props('style="font-size: 3rem"')

# 创建一个行容器，包含两个列容器
with ui.row():
   # 在第一个列容器中添加一个图标，内容为 B，颜色为橙色，大小为 4 rem
   ui.icon('B', color='orange', size="4rem")
   # 在第一个列容器中添加一个链接，内容为 "跳转到页面B"，跳转到 /funcB 页面
   ui.link("跳转到页面B", "/funcB").props('style="font-size: 3rem"')

# # 创建一个行容器，包含两个列容器
# with ui.row():
#     # 在第一个列容器中添加一个图标，内容为 C，颜色为橙色，大小为 4 rem
#     ui.icon('C', color='orange', size="4rem")
#     # 在第一个列容器中添加一个链接，内容为 "跳转到页面C"，跳转到 /funcC 页面
#     ui.link("跳转到页面C", "/funcC").props('style="font-size: 3rem"')

# 运行应用程序
ui.run()

