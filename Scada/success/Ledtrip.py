import struct
import time
import snap7

def plc_connect(ip, rack=0, slot=2):
    '''
    连接初始化
    :param ip:
    :param rack: 通常为0
    :param slot: 根据plc安装，一般为0或1
    :return:
    '''
    client = snap7.client.Client()
    client.connect(ip, rack, slot)
    return client

def plc_con_close(client):
    """
    连接关闭
    :param client:
    :return:
    """
    client.disconnect()

def ledtrip(client):
    """
    跑马灯，使Q0.0~5循环亮起
    :return:
    """
    area = snap7.types.Areas.PA
    dbnumber = 0
    start = 0
    delayTime = 0.3
    for i in range(1000):
        client.write_area(area, dbnumber, start, bytearray([0b00000001]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b00000010]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b00000100]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b00001000]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b00010000]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b00100000]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b01000000]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, bytearray([0b10000000]))
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\xff')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x40')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x20')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x10')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x08')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x04')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x02')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x01')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x00')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x11')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x22')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x44')
        time.sleep(delayTime)
        client.write_area(area, dbnumber, start, b'\x88')
        time.sleep(delayTime)
    client.write_area(area, dbnumber, start, b'\x00')


if __name__ == "__main__":
    client_fd = plc_connect('192.168.0.2')
    ledtrip(client_fd)
    plc_con_close(client_fd)