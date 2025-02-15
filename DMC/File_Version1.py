# -*- coding: utf-8 -*-
# 自动获取不断更新的文件，提取csv文件数据，并写入一个新的文件. 需解决： 存入的数据不再存
import os
import time
import threading


filepath = 'C:\\Natlqs\\Projects\\1# HSCB DMC Result Confirm\\Natlqs\\CSV'


def File_Save(filename):
    with open(filepath + '\\' + filename) as csvfile:
        reader = csvfile.readlines()
        values = reader[4].split(';')       # 获取第5行数据
        DMC = values[0]
        rotate_speed = values[7]
        ok_result = values[2]
        g_value = values[12]
        data_to_write = DMC + ';' + g_value
        if (ok_result == 'OK') & (rotate_speed == '180000'):
            this_week_csv = filepath + '\\' + \
                time.strftime('%Y%m%d %H:%M:%S', time.localtime(
                    get_week_begin(time.time(), 0)))[2:8] + '.csv'
            with open(this_week_csv, 'a') as file_destination:
                file_destination.write(data_to_write)
                file_destination.write('\n')
            pass


def Getfiles():     # 获取文件名
    '''
    扫描文件夹中的文件，删除8天前的，并返回所有文件的文件名
    '''
    filenames0 = os.listdir(filepath)
    n_daysago = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_day_begin(time.time(), -8)))[2:8]
    today = time.strftime('%Y%m%d %H:%M:%S', time.localtime(
        get_day_begin(time.time(), 0)))[2:8]
    for i in filenames0:
        if i[-17:-11] < n_daysago:      # 判断是否为8天前的文件
            a = filepath + '\\' + i
            os.remove(a)  # 如果是七天前的文件，删除
    global filenames
    filenames = os.listdir(filepath)


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
        if last_saturday > i[-17:-11]:  # < next_weekbegin:      # 判断文件是否为本周或上周六文件文件
            File_Save(i)
            pass
        else:
            pass


def Cycle_Refresh():
    print(time.time())
    Getfiles()
    print(time.time())
    File_Write()
    print(time.time())
    print('\n')
    print('finished')
    global t1
    t1 = threading.Timer(600, Cycle_Refresh)
    t1.start()


if __name__ == '__main__':
    Cycle_Refresh()
