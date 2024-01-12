from nicegui import ui
import ui_file, ui_charts, ui_table
import viewData
import sys

sys.stdout = open('mylog.txt', 'w', encoding='utf-8')
sys.stderr = open('myerr.txt', 'w', encoding='utf-8')

@ui.page('/')
def index():
    ui_file.build()
    ui_table.build()
    ui_charts.build()


ui.run(reload=False, native= True)