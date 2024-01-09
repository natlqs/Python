from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path
from nicegui import ui
# from my_ui import run_with

app = FastAPI()

ui.label("nicegui label")
# run_with(app)
ui.run_with(app)
