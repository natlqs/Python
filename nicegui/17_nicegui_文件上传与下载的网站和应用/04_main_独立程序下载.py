import pandas as pd
from nicegui import ui, app
import pandas as pd
import webview

df = pd.DataFrame({"name": list('abcd'), "value": [1, 2, 3, 4]})
async def onclick():
    file = await app.native.main_window.create_file_dialog(
        webview.SAVE_DIALOG, file_types=("excel文件 (*.xlsx;*.xls)", )
    )

    if file is not None:
        print(file)
        df.to_excel(file)


ui.button('导出Excel', on_click=onclick)
ui.aggrid.from_pandas(df)

ui.run(native=True)