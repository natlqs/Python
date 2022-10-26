# -*- coding: utf-8 -*-
# version1：自动获取不断更新的文件，提取csv文件数据，并写入一个新的文件,每个新文件存储本周日至周六及上周六的数据；
# version2:存入的数据不再存
# version3:增加Tk界面
import os
import time
import threading
import tkinter as tk
from tkinter import filedialog, scrolledtext


GUI = tk.Tk()    # 主窗口
GUI.title('1# HSCB Data G Value Result Automatically Save')
GUI.iconbitmap('')
GUI.geometry('400x230')


file_choose = tk.LabelFrame(GUI, text='文件路径选择', padx=6, pady=6)
file_choose.place(x=10, y=10)
file_choose_text_source = scrolledtext.ScrolledText(
    file_choose, width=25, height=3, padx=6, pady=6, wrap=tk.WORD)
file_choose_text_source.grid(column=0, row=0)
file_choose_text_destination = scrolledtext.ScrolledText(
    file_choose, width=25, height=3, padx=6, pady=10, wrap=tk.WORD)
file_choose_text_destination.grid(column=0, row=1)


start_switch = tk.LabelFrame(GUI, text='', padx=10, pady=10)
start_switch.place(x=115, y=165)


def Select_Source_Folder():
    global filepath_source
    filepath_source0 = filedialog.askdirectory()
    filepath_source = filepath_source0.replace('/', '\\')
    file_choose_text_source.insert('end', '\n' + str(filepath_source)+'\n')
    file_choose_text_source.config(bg='lightgreen')
    file_choose_text_source.see('end')


def Select_Destination_Folder():
    global filepath_destination
    filepath_destination0 = filedialog.askdirectory()
    filepath_destination = filepath_destination0.replace('/', '\\')
    file_choose_text_destination.insert(
        'end', '\n' + str(filepath_destination) + '\n')
    file_choose_text_destination.config(bg='lightgreen')
    file_choose_text_destination.see('end')


def File_Save(filename):
    with open(filepath_source + '\\' + filename) as csvfile:
        reader = csvfile.readlines()
        if len(reader) > 5:
            values = reader[4].split(';')       # 获取第5行数据
            DMC = values[0]
            rotate_speed = values[7]
            ok_result = values[2]
            g_value = values[12]
            data_time = values[4]
        # print(data_time)
            data_to_write = DMC + ';' + g_value + ';' + data_time+'\n'
            if (ok_result == 'OK') & (rotate_speed == '180000'):
                this_week_csv = filepath_destination + '\\' + \
                    time.strftime('%Y%m%d %H:%M:%S', time.localtime(
                        get_week_begin(time.time(), 0)))[2:8] + '.csv'
                with open(this_week_csv, 'a+') as new_file:
                    pass
                with open(this_week_csv, 'r+') as file_destination:
                    exist_data = file_destination.readlines()
                    if exist_data == []:
                        with open(this_week_csv, 'a+') as write0:
                            write0.write(data_to_write)
                    else:
                        if exist_data.count(data_to_write) > 0:
                            pass
                        else:
                            with open(this_week_csv, 'a') as file_destination:
                                file_destination.write(data_to_write)
            pass
        else:
            pass


def Getfiles():     # 获取文件名
    '''
    扫描文件夹中的文件，删除8天前的，并返回所有文件的文件名
    '''
    filenames0 = os.listdir(filepath_source)
    n_daysago = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_day_begin(time.time(), -8)))[2:8]
    today = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_day_begin(time.time(), 0)))[2:8]
    for i in filenames0:
        if (i[56:62] != '') & (i[56:62] < n_daysago):      # 判断是否为8天前的文件
            a = filepath_source + '\\' + i
            os.remove(a)  # 如果是七天前的文件，删除
          #  pass
    global filenames
    filenames = os.listdir(filepath_source)


def get_day_begin(ts=time.time(), N=0):     # 获取当天起始时间
    """
    N为0时获取时间戳ts当天的起始时间戳，N为负数时前数N天，N为正数是后数N天
    24 时(小时)=86400 000 毫秒
    """
    return int(time.mktime(time.strptime(time.strftime('%Y-%m-%d', time.localtime(ts)), '%Y-%m-%d'))) + 86400 * N


def get_week_begin(ts=time.time(), N=0):
    """
    N为0时获取时间戳ts当周的开始时间戳，N为负数时前数N周，N为整数是后数N周，此函数将周一作为周的第一天
    """
    w = int(time.strftime('%w', time.localtime(ts)))
    return get_day_begin(int(ts - w*86400)) + N*604800


def File_Write():
    '''
    保存上周六和本周的数据只本周csv文件
    '''
    this_weekbegin = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_week_begin(time.time(), 0)))[2:8]     # 本周开始日期,周日为第一天       211024
    next_weekbegin = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_week_begin(time.time(), 1)))[2:8]     # 下周开始日期, 周日为第一天       211031
    last_saturday = time.strftime('%Y%m%d %H:%M:%S', time.localtime(get_day_begin(
        get_week_begin(time.time(), 0)-86400, 0)))[2:8]       # 上周六        211023
    for i in filenames:
        if last_saturday < i[-17:-11]:  # < next_weekbegin:      # 判断文件是否为本周或上周六文件文件
            File_Save(i)
            pass
        else:
            pass


def Cycle_Refresh():
    Getfiles()
    File_Write()
    print('finish')
    global t1
    t1 = threading.Timer(60, Cycle_Refresh)
    t1.start()


tk.Button(start_switch, text='开始自动保存', font='宋体 13 bold',
          command=Cycle_Refresh).pack(padx=10)
tk.Button(file_choose, text='选择源数据文件夹', font='宋体 12 bold',
          command=Select_Source_Folder).grid(column=1, row=0)
tk.Button(file_choose, text='选择目的文件夹', font='宋体 12 bold',
          command=Select_Destination_Folder).grid(column=1, row=1)
GUI.mainloop()
