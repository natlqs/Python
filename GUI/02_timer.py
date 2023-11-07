# -*- coding:utf-8 -*-
import tkinter
import datetime


def uptime():
    global TimeLabel
    TimeLabel.config(text=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    win.after(200, uptime)


win = tkinter.Tk()
win.title("当前时间")
win.attributes("-topmost", True)
win.geometry("%dx%d" % (200, 50))

TimeLabel = tkinter.Label(
    text="%s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),)
)

TimeLabel.pack(fill=tkinter.BOTH, padx=10, pady=8)
win.after(100, uptime)
win.mainloop()
