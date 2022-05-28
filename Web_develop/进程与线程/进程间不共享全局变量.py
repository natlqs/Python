import multiprocessing
import time
my_list = []

def write_date():
    for i in range(3):
        my_list.append(i)
        print("add:", i)
    print("write_data", my_list)

def read_data():
    print("read_data", my_list)

if __name__ == "__main__":
    write_process = multiprocessing.Process(target=write_date)
    read_process = multiprocessing.Process(target=read_data)
    write_process.start()
    time.sleep(1)
    read_process.start()