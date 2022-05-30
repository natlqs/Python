# 导入进程模块
import time
import threading

# 编写函数
def coding(num):
    for i in range(num):
        print("coding...")
        time.sleep(0.2)

# 听音乐
def music(count):
    for i in range(count):
        print("music...")
        time.sleep(0.2)

if __name__ == "__main__":
    coding_process = threading.Thread(target=coding, args=(3,))
    music_process = threading.Thread(target=music, kwargs={"count":1})
    coding_process.start()
    music_process.start()
    