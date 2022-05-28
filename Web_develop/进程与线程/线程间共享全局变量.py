from asyncore import read
from concurrent.futures import thread
import imp
import threading
import time
from xml.dom.expatbuilder import theDOMImplementation

my_list = []

def write_data():
    for i in range(3):
        print("add", i)
        my_list.append(i)
    print("write", my_list)

def read_data():
    print("read", my_list)

if __name__ == "__main__":
    write_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)

    write_thread.start()
    time.sleep(1)
    read_thread.start()