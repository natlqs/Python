"""这个程序是一个使用FastAPI库编写的简单Web应用程序，用于展示页面之间的跳转和传递参数。程序定义了两个函数，
分别用于显示页面A和B的内容。
    1. func_A()：显示页面A的内容。函数返回一个HTML响应，其中包含一个HTML文件的内容。该HTML文件的内容可以从名为"a.html"的
    文件中读取。
    2. func_B()：显示页面B的内容。函数返回一个字符串，表示"Hello from function B"。
程序还定义了一个名为run_with的装饰器，用于将这两个函数注册到FastAPI应用中。装饰器接受一个FastAPI应用对象作为参数，
并将这两个函数分别注册为应用的GET请求处理程序。最后，程序使用Path库读取名为"a.html"的文件，将其内容作为HTML响应返回。"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path


def run_with(app: FastAPI):
    @app.get("/funcA")
    def func_A():
        return HTMLResponse(Path("static/a.html").read_bytes())

    @app.get("/funcB")
    def func_B():
        return "Hello from function B"
