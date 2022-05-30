from turtle import st
import snap7
import struct
import time

def plc_connect(ip, rack=0, slot = 2):
    '''
    鏈接初始化
    '''

    client = snap7.client.Client()
    client.connect(ip, rack, slot)
    return client

def plc_con_close(client):
    '''
    鏈接關閉
    '''
    client.disconnect()

def test_mk10_1(client):
    '''
    測試M10.1
    '''
    area = snap7.types.Areas.MK
    dbnumber = 0
    start = 10
    amount = 1
    print('初始值', end = '')
    mk_data = client.read_area(area, dbnumber, start, amount)
    print(mk_data)
    print('置1')
    client.write_area(area, dbnumber, start, b'\x01')
    print('當前值', end='')
    mk_cur = client.read_area(area, dbnumber, start, amount)
    print(mk_cur)


def test_q0_0(client):
    '''
    測試q0.0
    '''
    area = snap7.types.Areas.PA
    dbnumber = 0
    start = 0
    amount = 4
    print('初始值', end='')
    mk_data = client.read_area(area, dbnumber, start, amount)
    print(mk_data)
    print('置1')
    client.write_area(area, dbnumber, start, b'\x01')
    print('當前值', end='')
    mk_cur = client.read_area(area, dbnumber, start, amount)
    print(mk_cur)


if __name__ == '__main__':
    client_fd = plc_connect('192.168.0.2')
    test_mk10_1(client_fd)
    test_q0_0(client_fd)
    plc_con_close(client_fd)