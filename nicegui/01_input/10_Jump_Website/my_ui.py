from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

def run_with(app:FastAPI):
    @app.get('/funcA')
    def func_A():
        return HTMLResponse (Path('static/a.html').read_bytes())


    @app.get('/funcB')
    def func_B():
        return "Hello from function B"