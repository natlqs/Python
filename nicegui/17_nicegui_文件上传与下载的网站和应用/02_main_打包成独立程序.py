import pandas as pd
from nicegui import ui, events, app
from pathlib import Path
import os, io

# 将 NiceGUI 界面中的内容设置为水平居中显示
ui.query(".nicegui-content").classes("flex-center")  # 将 NiceGUI 界面中的内容设置为水平居中显示
# 1. 使用 ui.query(".nicegui-content") 选择 class 名为 "nicegui-content" 的 HTML 元素。
# 2. 使用 .classes("flex-center") 为该元素添加名为 "flex-center" 的 class。

async def choose_file():
    files = await app.native.main_window.create_file_dialog(
        file_types=("excel文件 (*.xlsx;*.xls)",)
    )
    if files is not None:
        # 使用BytesIO对象显示为pandas data frame
        print(files)
        df = pd.read_excel(files[0])
        ui.aggrid.from_pandas(df)
        with open(files[0], "rb") as f :
            data = f.read()
        Path(os.path.dirname(__file__) + "\\temp.xlsx").write_bytes(data)

# 创建一个上传文件的输入元素
ui.button("上传excel文件", on_click=choose_file)
# 运行应用程序
ui.run(native=True)
