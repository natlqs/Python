# 扫码显示成功, 比较功能没有
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

file_name=['']


SerialPort = serial.Serial()
GUI = tk.Tk()  # 父容器
GUI.title("1# HSCB G Value Result Check")  # 父容器标题
GUI.iconbitmap('C:\\Natlqs\Projects\\1# HSCB DMC Result Confirm\\icon.ico')
GUI.geometry("1024x668")  # 父容器大小
 
#Information = tk.LabelFrame(GUI, text="操作信息", padx=10, pady=10)  # 水平，垂直方向上的边距均为10
#Information.place(x=20, y=20)
#Information_Window = scrolledtext.ScrolledText(Information, width=20, height=5, padx=10, pady = 10,wrap = tk.WORD)
#Information_Window.grid()
 
#Send = tk.LabelFrame(GUI, text="发送指令", padx=10, pady=5)  # 水平，垂直方向上的边距均为 10
#Send.place(x=240, y=20)
 
#DataSend = tk.StringVar()  # 定义DataSend为保存文本框内容的字符串
 
#EntrySend = tk.StringVar()
#Send_Window = ttk.Entry(Send, textvariable=EntrySend, width=23)
#Send_Window.grid()
 
 
'''def WriteData():
    global DataSend
    DataSend = EntrySend.get()
    Information_Window.insert("end", '发送指令为：' + str(DataSend) + '\n')
    Information_Window.see("end")
    SerialPort.write(bytes(DataSend, encoding='utf8'))
'''
 
#tk.Button(Send, text="发送", command=WriteData).grid(pady=5, sticky=tk.E)
 
Receive = tk.LabelFrame( GUI, text = "端口状态", font='宋体 15 bold', padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为 10
Receive.place(x = 20, y = 180)
Receive_Window = scrolledtext.ScrolledText(Receive, width = 34, height = 4, padx = 8, pady = 10,wrap = tk.WORD)
Receive_Window.grid()
 
option = tk.LabelFrame( GUI, text = "串口选项",font='宋体 15 bold', padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为10
option.place(x = 20, y = 20, width = 300)  # 定位坐标
# ************创建下拉列表**************
ttk.Label( option, text = "串口号:" ,font='宋体 15 bold').grid( column = 0, row = 0 )  # 添加串口号标签
ttk.Label( option, text = "波特率:" ,font='宋体 15 bold').grid( column = 0, row = 1 )  # 添加波特率标签


file_choose=tk.LabelFrame(GUI, text='源文件选择', font='宋体 15 bold', padx=10, pady=10)
file_choose.place(x=20, y=300)
file_choose_text=scrolledtext.ScrolledText(file_choose,width=34,height=4, padx=10, pady=10, wrap=tk.WORD)
file_choose_text.grid()
file_choose_text.insert(tk.INSERT, '')


compare_result=tk.LabelFrame(GUI, text='检查结果', font='宋体 20 bold', padx=10, pady=10)
compare_result.place(x=370, y=120)
compare_result=scrolledtext.ScrolledText(compare_result, font='宋体 20 bold', width=30,height=10, padx=10, pady=10)
compare_result.grid()


Port = tk.StringVar()  # 端口号字符串
Port_list = ttk.Combobox( option, width = 15,font='宋体 15 bold', textvariable = Port, state = 'readonly' )
ListPorts = list(serial.tools.list_ports.comports())
Port_list['values'] = [i[0] for i in ListPorts]
Port_list.current(0)
Port_list.grid(column=1, row=0)  # 设置其在界面中出现的位置  column代表列   row 代表行
 
BaudRate = tk.StringVar()  # 波特率字符串
BaudRate_list = ttk.Combobox( option, width = 15,font='宋体 15 bold', textvariable = BaudRate, state = 'readonly' )
BaudRate_list['values'] = (1200, 2400, 4800, 9600, 14400, 19200, 38400, 43000, 57600, 76800, 115200)
BaudRate_list.current(3)
BaudRate_list.grid(column=1, row=1)  # 设置其在界面中出现的位置  column代表列   row 代表行
 
switch = tk.LabelFrame( GUI, text = "", padx = 10, pady = 10 )  # 水平，垂直方向上的边距均为 10
switch.place(x = 20, y = 120, width = 300)  # 定位坐标


switch1= tk.LabelFrame(GUI, text='', padx=10, pady=10)
switch1.place(x=420, y=20)

def File_Choose_Button():
    file_path=filedialog.askopenfilename()
    print(file_path)
    file_path=file_path.replace('/', '\\')
    print(file_path)
    file_choose_text.insert('end', '\n'+str(file_path)+ '\n')
    file_choose_text.see('end')
    file_name[0]=file_path
   
  
def ReceiveData():
    
    while SerialPort.isOpen():
        DMC=str(SerialPort.readline())
        if DMC=="b''":
            pass
        else:
            #Receive_Window.insert("end", DMC + '\n')
            #Receive_Window.see("end")
            compare_result.insert('end', 'DMC:'+DMC[2:-5]+ '\n')
            # compare_result.insert('end', file_name+ '\n')
            # compare_result.insert('end', 'true'+'\n')
            compare_result.insert('end', file_name[0]+'\n'+'\n'+'\n'+'\n')
            
            compare_result.see('end')

def Close_Serial():
    SerialPort.close()
    Receive_Window.insert('end', Port_list.get()+'端口已关闭'+ '\n')
 

def Open_Serial():
    if not SerialPort.isOpen():
        SerialPort.port = Port_list.get()
        SerialPort.baudrate = BaudRate_list.get()
        SerialPort.timeout = 0.1
        SerialPort.open()
        Receive_Window.insert('end', Port_list.get()+'端口已打开'+ '\n')
        
    else:
        SerialPort.close()
        Receive_Window.insert('end', Port_list.get()+'端口打开失败，请检查端口是否占用'+'\n')


def Start_Compare():
    if SerialPort.isOpen():
            t = threading.Thread(target=ReceiveData)
            t.setDaemon(True)
            t.start()
    pass


def Stop_Compare():
    pass
 
 
tk.Button( switch, text = "打开端口",font='宋体 15 bold', command = Open_Serial ).pack( side = "left", padx = 8 )
tk.Button( switch, text = "关闭端口",font='宋体 15 bold', command = Close_Serial ).pack( side = "right", padx = 8 )
tk.Button(switch1, text='开始检查', font='宋体 25 bold', command=Start_Compare).pack(side='left', padx=10)
tk.Button(switch1, text='停止检查', font='宋体 25 bold', command=Stop_Compare).pack(side='left', padx=10)
tk.Button( file_choose, text='选择源文件', font='宋体 15 bold', command = File_Choose_Button).grid(row=1, column=0, pady=20)
GUI.mainloop()