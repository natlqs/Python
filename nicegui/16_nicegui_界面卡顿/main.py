import time
from nicegui import ui, run

# 定义一个函数，用于操作 class 名为 "nicegui-content" 的 HTML 元素，并为该元素添加名为 "flex-center" 的 class
ui.query(".nicegui-content").classes("flex-center")

# 定义一个函数，用于执行任务1，任务1将在8秒后完成
def task1():
   time.sleep(8)

# 定义一个异步函数，用于执行任务2，任务2将在指定时间（默认为5秒）后完成
def task2(_time:int=5):
   time.sleep(_time)

# 定义一个异步函数，用于执行任务3，任务3将在指定时间（默认为10秒）后完成
def task3(_time: int=10):
   time.sleep(_time)

# 定义一个函数，用于构建任务加载的界面
def build_task_loading(message: str, is_done=False):
   with ui.row().classes("flex-center"):
       if not is_done:
           ui.spinner(color="negative")
       else:
           ui.icon("done", color="positive")
       with ui.row():
           ui.label(message)

# 定义一个异步函数，用于执行所有任务
async def run_tasks():
   loading = ui.refreshable(build_task_loading)
   loading1 = ui.refreshable(build_task_loading)
   loading("任务A")
   loading1("任务D")
   await run.io_bound(task1)
   loading.refresh("任务A结束", is_done=True)
   loading1.refresh("任务D结束", is_done=True)

   loading = ui.refreshable(build_task_loading)
   loading("任务b")
   await run.io_bound(task2)
   loading.refresh("任务b结束", is_done=True)

   loading = ui.refreshable(build_task_loading)
   loading("任务c")
   await run.io_bound(task3)
   loading.refresh("任务c结束", is_done=True)

# 定义一个按钮，用于启动所有任务
ui.button("执行", color="red", on_click=run_tasks)

# 运行 ui
ui.run()
