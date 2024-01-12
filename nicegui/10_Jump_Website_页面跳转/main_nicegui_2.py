''' 这是一个使用nicegui库编写的简单Web应用程序，用于展示一个简单的页面，其中包含一个标签和一个输入框。当输入框的值发生变化时，
标签的文本也会相应地发生变化。
1. `index_page()`：定义默认根路径下的页面。函数中添加了一个标签和一个输入框。标签显示为"默认根路径下"。
输入框的文本被绑定到名为`content`的标签上，当输入框的值发生变化时，标签的文本也会相应地发生变化。
2. `onchange()`：定义输入框的`on_change`事件处理函数。当输入框的值发生变化时，函数会被调用，并将输入框的值赋值给`content`标签。
3. `ui.run()`：启动应用程序。'''


from nicegui import ui


@ui.page("/")
def index_page():
    ui.label("默认根路径下")

    def onchange():
        content.text = input.value

    content = ui.label('')
    input = ui.input("修改标签值", on_change=onchange)


ui.run()