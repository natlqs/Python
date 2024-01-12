import os
import subprocess
from pathlib import Path
import nicegui
import ex4nicegui
import pyecharts

cmd = [
    "PyInstaller",
    "main.py",  # your main file with ui.run()
    "--name",
    "myapp",  # name of your app
    "--onefile",
    "--windowed",
    "--clean",
    #'--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    "--add-data",
    f"{Path(nicegui.__file__).parent}{os.pathsep}nicegui",
    "--add-data",
    f"{Path(ex4nicegui.__file__).parent}{os.pathsep}ex4nicegui",
    "--add-data",
    f"{Path(pyecharts.__file__).parent}{os.pathsep}pyecharts",
]

subprocess.call(cmd)
