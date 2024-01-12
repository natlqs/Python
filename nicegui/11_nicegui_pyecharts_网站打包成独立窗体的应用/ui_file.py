from nicegui import ui, app
from ex4nicegui.reactive import rxui
import viewData
from ex4nicegui import to_ref, on

# 定义一个名为 NativeFileChooser 的类
class NativeFileChooser:
   # 构造函数，初始化 _selected 属性
   def __init__(self) -> None:
       # 返回 _selected 属性
       self._selected = to_ref("")
   
   # 定义一个名为 selected 的属性，使用 @property 装饰器装饰
   @property
   def selected(self):
       # 返回 _selected 属性
       return self._selected
   
   # 定义一个名为 open 的异步方法，用于打开文件对话框选择文件
   async def open(self):
       # 创建文件对话框，文件类型为 ("excel文件（*.xlsx)",)
       files = await app.native.main_window.create_file_dialog(
           file_types=("excel文件 (*.xlsx)",)
       )

       # 将选中的文件路径设置给 _selected 属性
       self._selected.value = files[0] if files else ""

   # 定义一个名为 bind_ref 的方法，用于将 _selected 属性的变化传递给 ref 引用的对象
   def bind_ref(self, ref):
       # 使用 on 装饰器监听 _selected 属性的变化
       @on(self._selected)
       # 定义一个函数，当 _selected 属性发生变化时，将 _selected.value 赋值给 ref.value
       def _():
           ref.value = self._selected.value


def build():
   # 创建一个 NativeFileChooser 对象
   fp = NativeFileChooser()
   
   # 将 fp 绑定到 viewData.r_current_file 引用的对象
   fp.bind_ref(viewData.r_current_file)
   
   # 使用 ui.expansion 创建一个展开的Card，标题为 "文件加载"，初始值为 True
   with ui.expansion("文件加载", value=True), ui.card(), ui.grid(columns=2).classes(
       "place-items-center"
   ):
       # 使用 ui.badge 创建一个带有 "文件:" 的标签，当点击时会调用 fp.open 方法
       file_badge = ui.badge("文件:")
       file_badge.on("click", fp.open)
       
       # 为 file_badge 添加 Tailwind CSS 样式，设置光标为 "pointer"，内边距为 "p-1.5"
       file_badge.tailwind.cursor("pointer").padding("p-1.5")
       
       # 使用 ui.label 创建一个 "文件：" 的标签
       #ui.label(“文件：”)
       
       # 使用 rxui.label 创建一个显示 viewData.r_current_file 引用的值的标签
       rxui.label(viewData.r_current_file)
       
       # 使用 ui.label 创建一个 "工作表" 的标签
       ui.label("工作表")
       
       # 使用 rxui.select 创建一个下拉选择框，显示 viewData.sheet_names 引用的值，
       # 并将 viewData.r_current_sheet 引用的值作为默认值，可清除
       rxui.select(
           viewData.sheet_names, value=viewData.r_current_sheet, clearable=True
       )
