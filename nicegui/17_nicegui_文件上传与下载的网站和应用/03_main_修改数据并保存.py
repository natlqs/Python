from fastapi.responses import StreamingResponse
from starlette.responses import ContentStream
from nicegui import ui, app
import pandas as pd
import io
import uuid

def download_stream(content: ContentStream, filename:str):
    download_path = f"/download/{uuid.uuid4()}"

    @app.get(download_path)
    def download():
        try:
            headers = {"Content-Disposition": f"attachment; filename={filename}"}
            return StreamingResponse(content, headers=headers)
        finally:
            app.remove_route(download_path)

    ui.download(download_path)

df = pd.DataFrame({"name":list("abcd"), "value":range(4)})

def onclick():
    data_io = io.BytesIO()
    df.to_excel(data_io)
    data_io.seek(0)

    download_stream(data_io, "download.xlsx")

ui.button("下载数据", on_click=onclick)
ui.aggrid.from_pandas(df)

ui.run()