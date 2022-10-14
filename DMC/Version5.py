#  扫码OK, 检查数据OK--fw  2021-10-21-20：25
#! /usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import tkinter as tk
from tkinter import Button, font
from tkinter import filedialog
from numpy.lib.arraypad import pad
from numpy.lib.function_base import insert
from openpyxl.descriptors.excel import Guid
import serial.tools.list_ports
from tkinter import ttk
from tkinter import scrolledtext
import xlrd
import time

DMC = ['']
file_name = ['']


SerialPort = serial.Serial()
GUI = tk.Tk()  # 主窗口
GUI.title("1# HSCB G Value Result Check")  # 父容器标题
GUI.iconbitmap('C:\\Natlqs\Projects\\1# HSCB DMC Result Confirm\\icon.ico')
GUI.geometry("890x450")  # 主窗口大小


Receive = tk.LabelFrame(GUI, text="端口状态", font='宋体 15 bold',
                        padx=10, pady=10)  # 水平，垂直方向上的边距均为 10
Receive.place(x=20, y=120)
Receive_Window = scrolledtext.ScrolledText(
    Receive, font='宋体 12 bold', width=28, height=4, padx=8, pady=10, wrap=tk.WORD)
Receive_Window.grid()


option = tk.LabelFrame(GUI, text="串口选项", font='宋体 15 bold',
                       padx=10, pady=10)  # 水平，垂直方向上的边距均为10
option.place(x=20, y=20, width=310)  # 定位坐标
# ************创建下拉列表**************
ttk.Label(option, text="串口号:", font='宋体 15 bold').grid(
    column=0, row=0)  # 添加串口号标签
ttk.Label(option, text="波特率:", font='宋体 15 bold').grid(
    column=0, row=1)  # 添加波特率标签


file_choose = tk.LabelFrame(
    GUI, text='源文件选择', font='宋体 15 bold', padx=10, pady=10)
file_choose.place(x=20, y=260)
file_choose_text = scrolledtext.ScrolledText(
    file_choose, width=36, height=4, padx=10, pady=10, wrap=tk.WORD)
file_choose_text.grid()
file_choose_text.insert(tk.INSERT, '')


compare_result = tk.LabelFrame(
    GUI, text='检查结果', font='宋体 20 bold', padx=10, pady=10)
compare_result.place(x=370, y=120)
compare_result = scrolledtext.ScrolledText(
    compare_result, font='宋体 15 bold', width=40, height=10, padx=10, pady=10)
compare_result.grid()


Port = tk.StringVar()  # 端口号字符串
Port_list = ttk.Combobox(option, width=15, font='宋体 15 bold',
                         textvariable=Port, state='readonly')
ListPorts = list(serial.tools.list_ports.comports())
Port_list['values'] = [i[0] for i in ListPorts]
Port_list.current(0)
Port_list.grid(column=1, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行

BaudRate = tk.StringVar()  # 波特率字符串
BaudRate_list = ttk.Combobox(
    option, width=15, font='宋体 15 bold', textvariable=BaudRate, state='readonly')
BaudRate_list['values'] = (1200, 2400, 4800, 9600,
                           14400, 19200, 38400, 43000, 57600, 76800, 115200)
BaudRate_list.current(3)
BaudRate_list.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行


# switch = tk.LabelFrame( GUI, text = "", padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为 10
# switch.place(x = 20, y = 120, width = 300)  # 定位坐标


switch1 = tk.LabelFrame(GUI, text='', padx=10, pady=10)
switch1.place(x=370, y=20)


def File_Choose_Button():
    file_path = filedialog.askopenfilename()
    file_path = file_path.replace('/', '\\')
    file_choose_text.insert('end', '\n'+str(file_path) + '\n')
    file_choose_text.see('end')
    file_name[0] = file_path


def ReceiveData():

    while SerialPort.isOpen():
        try:
            DMC[0] = str(SerialPort.readline())
        except:
            pass
        if DMC[0] == "b''":
            pass
        else:
            compare_result.insert('end', '\n'+'\n' + '时间： ')
            compare_result.insert('end', time.localtime())
            compare_result.insert(
                'end', '\n'+'\n' + 'DMC:' + DMC[0][2:-5] + '\n')
            Compare_Result()
            compare_result.see('end')


def Compare_Result():
    workbook = xlrd.open_workbook(file_name[0])
    sheet = workbook.sheet_by_index(0)          # 读取源excel文件第m个sheet的内容
    nrowsnum = sheet.nrows        # 获取该shee的行数
    for i in range(0, nrowsnum):
        date = sheet.row(i)       # 获取i行的内容
        value = str(date[0])        # 把第n个单元格转化为字符串，目的是下一步的关键字比对
        if value.find(DMC[0][2:-5]) > 0:      # 与关键字比对，包含的返回1， 否则返回0
            if date[1].value > 17:
                compare_result.insert(
                    'end', '\n' + 'G 值结果：' + '专用F202' + '\n'*4)
            else:
                compare_result.insert(
                    'end', '\n' + 'G 值结果：' + '非专用F202'+'\n'*4)
        else:
            if i < nrowsnum-1:
                pass
            else:
                compare_result.insert(
                    'end', '\n' + 'G 值结果：' + '没找到该产品记录' + '\n'*4)


def Close_Serial():
    SerialPort.close()
    Receive_Window.insert('end', '时间： ')
    Receive_Window.insert('end', time.localtime())
    Receive_Window.insert('end', '\n' + Port_list.get()+'端口已关闭' + '\n')
    Receive_Window.see('end')


def Open_Serial():
    if not SerialPort.isOpen():
        SerialPort.port = Port_list.get()
        SerialPort.baudrate = BaudRate_list.get()
        SerialPort.timeout = 0.1
        SerialPort.open()
        Receive_Window.insert('end', '时间： ')
        Receive_Window.insert('end', time.localtime())
        Receive_Window.insert('end', '\n' + Port_list.get()+'端口已打开' + '\n')
        Receive_Window.see('end')
    else:
        SerialPort.close()
        Receive_Window.insert('end', '时间： ')
        Receive_Window.insert('end', time.localtime())
        Receive_Window.insert(
            'end', '\n' + Port_list.get()+'端口打开失败，请检查端口是否占用'+'\n')
        Receive_Window.see('end')


def Start_Compare():
    if file_name[0] == '':
        compare_result.insert('end', '\n' + '\n' + '时间： ')
        compare_result.insert('end', time.localtime())
        compare_result.insert('end', '\n' + '请先选择源文件' + '\n'*6)
    else:
        if SerialPort.isOpen():
            t = threading.Thread(target=ReceiveData)
            t.setDaemon(True)
            t.start()
    pass


def Stop_Compare():
    t = threading.Thread(target=Close_Serial)
    t.setDaemon(True)
    t.start()
    pass


tk.Button(switch1, text="打开端口", font='宋体 22 bold',
          command=Open_Serial).pack(side="left", padx=8)
tk.Button(switch1, text='开始检查', font='宋体 22 bold',
          command=Start_Compare).pack(side='left', padx=8)
tk.Button(switch1, text="关闭端口", font='宋体 22 bold',
          command=Close_Serial).pack(side="left", padx=8)
# tk.Button(switch1, text='停止检查', font='宋体 25 bold', command=Stop_Compare).pack(side='left', padx=10)
tk.Button(file_choose, text='选择源文件', font='宋体 15 bold',
          command=File_Choose_Button).grid(row=1, column=0, pady=10)
GUI.mainloop()
