# 这是一个使用 NiceGUI 库创建的界面，用于上传 Excel 文件。
# 当用户选择要上传的 Excel 文件并点击“上传”按钮时，将触发 on_upload 函数。该函数将读取上传的文件内容并将其保存到临时文件中。
import pandas as pd
from nicegui import ui, events, app
from pathlib import Path
import os, io

# 将 NiceGUI 界面中的内容设置为水平居中显示
ui.query(".nicegui-content").classes("flex-center")  # 将 NiceGUI 界面中的内容设置为水平居中显示
# 1. 使用 ui.query(".nicegui-content") 选择 class 名为 "nicegui-content" 的 HTML 元素。
# 2. 使用 .classes("flex-center") 为该元素添加名为 "flex-center" 的 class。


# 定义一个上传文件的函数，当用户选择文件并点击“上传”按钮时，将触发该函数
def on_upload(e: events.UploadEventArguments):
    # print(e)
    # print("当前文件所在的目录：" + os.path.dirname(__file__))

    # 将上传的文件内容读取到BytesIO对象中
    file_content = io.BytesIO(e.content.read())

    # 使用BytesIO对象显示为pandas data frame
    df = pd.read_excel(file_content)
    ui.aggrid.from_pandas(df)

    # 将其内容保存到文件中
    # 读取上传的文件内容并将其保存到临时文件中
    Path(os.path.dirname(__file__) + "\\temp.xlsx").write_bytes(e.content.read())

# 创建一个上传文件的输入元素
ui.upload(label="上传excel文件", auto_upload=True, on_upload=on_upload).props(
    'accept=".xlsx"'
)
# 运行应用程序
ui.run()
