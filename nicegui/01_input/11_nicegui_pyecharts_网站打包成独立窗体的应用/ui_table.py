from nicegui import ui
from ex4nicegui.reactive import rxui
import viewData

def build():
   # 添加一个分割线
   ui.separator()

   # 使用 rxui.expansion 创建一个可展开的Card，标题为 "表格"，并将其绑定到 viewData.showTable 引用的对象
   with rxui.expansion("表格").classes("w-full").bind_visible(viewData.can_load_data):
       # 使用 rxui.aggird.from_pandas 创建一个表格，表格数据来自 viewData.data 引用的对象
       rxui.aggird.from_pandas(viewData.data, auto_size_columns=False)
