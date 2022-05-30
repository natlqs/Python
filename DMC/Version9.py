#  已添加根据检查结果更换颜色功能, 并已完善界面及提示
# Version 9 : 所有功能测试ok，需完善界面
#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import threading
import binascii
import struct
import tkinter as tk
from tkinter import Button, font
from tkinter import filedialog
import serial.tools.list_ports
from tkinter import ttk
from tkinter import scrolledtext
import time
import datetime
import csv


DMC=['']
file_name=['']

SerialPort = serial.Serial()
GUI = tk.Tk()  # 主窗口
GUI.title("1# HSCB G Value Result Check")  # 父容器标题
# GUI.iconbitmap('C:\\Natlqs\Projects\\1# HSCB DMC Result Confirm\\icon.ico')
GUI.geometry("720x405")  # 主窗口大小
GUI.wm_attributes('-topmost', 1)

Receive = tk.LabelFrame( GUI, text = "端口状态", font='宋体 15 bold', padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为 10
Receive.place(x = 5, y = 105)
Receive_Window = scrolledtext.ScrolledText(Receive,font='宋体 12 bold', width = 28, height = 4, padx = 8, pady = 10,wrap = tk.WORD)
Receive_Window.grid()
 

option = tk.LabelFrame( GUI, text = "串口选项",font='宋体 15 bold', padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为10
option.place(x = 5, y = 5, width = 310)  # 定位坐标
# ************创建下拉列表**************
ttk.Label( option, text = "串口号:" ,font='宋体 15 bold').grid( column = 0, row = 0 )  # 添加串口号标签
ttk.Label( option, text = "波特率:" ,font='宋体 15 bold').grid( column = 0, row = 1 )  # 添加波特率标签


file_choose=tk.LabelFrame(GUI, text='源文件夹选择', font='宋体 15 bold', padx=10, pady=10)
file_choose.place(x=5, y=240)
file_choose_text=scrolledtext.ScrolledText(file_choose,width=36,height=4, padx=10, pady=10, wrap=tk.WORD)
file_choose_text.grid()
file_choose_text.insert(tk.INSERT, '')


compare_result_frame=tk.LabelFrame(GUI, text='检查结果',  font='宋体 20 bold', padx=10, pady=10)
compare_result_frame.place(x=320, y=100)
compare_result_text=scrolledtext.ScrolledText(compare_result_frame,bg='white', font='宋体 15 bold', width=30,height=10, padx=10, pady=10)
compare_result_text.grid()
compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
compare_result_text.insert('end', '\n'+ '欢迎使用1# HSCB G值检查程序,请选择并打开端口' + '\n'*5)
compare_result_text.config(bg='white')
compare_result_text.see('end')


Port = tk.StringVar()  # 端口号字符串
Port_list = ttk.Combobox( option, width = 15,font='宋体 15 bold', textvariable = Port, state = 'readonly' )
ListPorts = list(serial.tools.list_ports.comports())
Port_list['values'] = [i[0] for i in ListPorts]
Port_list.current(0)
Port_list.grid(column=1, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行
 
BaudRate = tk.StringVar()  # 波特率字符串
BaudRate_list = ttk.Combobox( option, width = 15,font='宋体 15 bold', textvariable = BaudRate, state = 'readonly' )
BaudRate_list['values'] = (1200, 2400, 4800, 9600, 14400, 19200, 38400, 43000, 57600, 76800, 115200)
BaudRate_list.current(10)
BaudRate_list.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行


switch1= tk.LabelFrame(GUI, text='', padx=10, pady=10)
switch1.place(x=320, y=15)

def File_Choose_Button():
    file_path=filedialog.askdirectory()
    file_path=file_path.replace('/', '\\')
    file_choose_text.insert('end', '\n'+str(file_path)+ '\n')
    file_choose_text.config(bg='lightgreen')
    file_choose_text.see('end')
    file_name[0]=file_path
   
  
def ReceiveData():
    while SerialPort.isOpen():
        try:
            DMC[0]=str(SerialPort.readline())
        except:
            pass
        if DMC[0]=="b''" or DMC[0] == "b'\\r\\n'" or len(DMC[0][2:-5]) < 31:
            pass
        else:
            compare_result_text.insert('end', '\n'+'\n'+ '时间： ')
            compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            compare_result_text.insert('end', '\n'+ 'DMC:' + DMC[0][2:-5]+ '\n')
            Compare_Result()
            compare_result_text.see('end')


def Compare_Result():
    this_week_csv = file_name[0] + '\\' + time.strftime('%Y%m%d %H:%M:%S', time.localtime(get_week_begin(time.time(),0)))[2:8] + '.csv'
    try:
        with open(this_week_csv, 'r') as read_data:
            data = read_data.readlines()
            x = 0
            time0 = '1990-01-01 00:00:00'
            g_value0 = 'ee'
            for i in data:
                length = len(data)
                i_split = i.split(';')
                DMC_time = i_split[2][0:-1]
                if x <= length:
                    if DMC[0][2:-5]==i_split[0]:
                        if (i_split[2][0:-1]>time0):
                            time0 = i_split[2][0:-1]
                            g_value0 = i_split[1]
                        else:
                            pass
            if g_value0=='ee':
                compare_result_text.insert('end', '\n' + 'G 值结果：'+ '没找到该产品记录'+ '\n'*3)
                compare_result_text.config(bg='red')
                compare_result_text.insert('end', '\n' + '请扫描下一个产品二维码'+ '\n')
            else:
                if float(g_value0)<16500:
                    compare_result_text.insert('end', '\n' + 'G 值结果：' + '专用F202'+'\n'*3)
                    compare_result_text.config(bg='lightgreen')
                    compare_result_text.insert('end', '\n' + '请扫描下一个产品二维码'+ '\n')
                    pass
                else:
                    compare_result_text.insert('end', '\n' + 'G 值结果：' + '非专用F202'+ '\n'*3)
                    compare_result_text.config(bg='#FE8C00')  
                    compare_result_text.insert('end', '\n' + '请扫描下一个产品二维码'+ '\n')
    except:
        compare_result_text.insert('end', '\n' + '文件未找到，请检查源文件路径是否正确' + '\n')
        compare_result_text.config(bg='red')  
        compare_result_text.insert('end', '\n' + '请检查源文件'+ time.strftime('%Y%m%d %H:%M:%S', time.localtime(get_week_begin(time.time(),0)))[2:8] + '.csv' + '是否存在' + '\n')
        pass


def Close_Serial():
    SerialPort.close()
    Receive_Window.insert('end', '时间： ')
    Receive_Window.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    Receive_Window.insert('end', '\n'+ Port_list.get()+'端口已关闭'+ '\n')
    Receive_Window.config(bg='#FF4500')
    Receive_Window.see('end')

    compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
    compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    compare_result_text.insert('end', '\n'+ '端口已关闭，检查停止' + '\n'*6)
    compare_result_text.config(bg='#FF4500')
    compare_result_text.see('end')
 

def Open_Serial():
    if not SerialPort.isOpen():
        SerialPort.port = Port_list.get()
        SerialPort.baudrate = BaudRate_list.get()
        SerialPort.bytesize = 8
        SerialPort.parity = serial.PARITY_NONE
        SerialPort.stopbits = 1
        SerialPort.timeout = 0.1
        SerialPort.open()
        Receive_Window.insert('end', '时间： ')
        Receive_Window.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        Receive_Window.insert('end', '\n'+ Port_list.get()+'端口已打开'+ '\n'*2)
        Receive_Window.config(bg='lightgreen')
        Receive_Window.see('end')

        compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
        compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        compare_result_text.insert('end', '\n'+ '端口已打开,请选择源文件夹并点击“开始检查”' + '\n'*6)
        compare_result_text.config(bg='#FFD700')
        compare_result_text.see('end')
 

    else:
        SerialPort.close()
        Receive_Window.insert('end', '时间： ')
        Receive_Window.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        Receive_Window.insert('end', '\n'+ Port_list.get()+'端口打开失败，请检查端口是否占用'+'\n')
        Receive_Window.config(bg='#ff4500')
        Receive_Window.see('end')


        compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
        compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        compare_result_text.insert('end', '\n'+ '端口打开失败，检查并重新打开端口' + '\n'*6)
        compare_result_text.config(bg='#FF4500')
        compare_result_text.see('end')

def Start_Compare():
    if not SerialPort.isOpen():
        compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
        compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        compare_result_text.insert('end', '\n'+ '请先选择并打开端口，选择源文件夹' + '\n'*6)
        compare_result_text.config(bg='#FF4500')
        compare_result_text.see('end')
    else:
        if file_name[0] == '':
            compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
            compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            compare_result_text.insert('end', '\n'+ '端口已打开，请先选择源文件夹' + '\n'*6)
            compare_result_text.config(bg='#FF8C00')
            compare_result_text.see('end')
        else:
            compare_result_text.insert('end', '\n'+ '\n'+ '时间： ')
            compare_result_text.insert('end', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            compare_result_text.insert('end', '\n'+ '开始检查， 请扫描产品二维码' + '\n'*6)
            compare_result_text.config(bg='lightyellow')
            compare_result_text.see('end')
    if SerialPort.isOpen():
        t = threading.Thread(target=ReceiveData)
        t.setDaemon(True)
        t.start()
    pass


def Stop_Compare():
    t=threading.Thread(target=Close_Serial)
    t.setDaemon(True)
    t.start()
    pass
 
 
def get_day_begin(ts=time.time(), N=0):     # 获取当天起始时间
    """
    N为0时获取时间戳ts当天的起始时间戳，N为负数时前数N天，N为正数是后数N天
    24 时(小时)=86400 000 毫秒
    """
    return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(ts)), '%Y-%m-%d'))) + 86400 * N


def get_week_begin(ts = time.time(),N = 0):
    """
    N为0时获取时间戳ts当周的开始时间戳，N为负数时前数N周，N为整数是后数N周，此函数将周一作为周的第一天
    """
    w = int(time.strftime('%w',time.localtime(ts)))
    return get_day_begin(int(ts - w*86400)) + N*604800





tk.Button(switch1, text = "打开端口",font='宋体 18 bold', command = Open_Serial ).pack( side = "left", padx = 2 )
tk.Button(switch1, text='开始检查', font='宋体 18 bold', command=Start_Compare).pack(side='left', padx=2)
tk.Button(switch1, text = "关闭端口",font='宋体 18 bold', command = Close_Serial ).pack( side = "left", padx = 2 )
tk.Button( file_choose, text='选择源文件', font='宋体 15 bold', command = File_Choose_Button).grid(row=1, column=0, pady=2)

GUI.mainloop()