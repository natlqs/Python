# 导入进程模块
import time
import threading

# 编写函数
def coding():
    for i in range(3):
        print("coding...")
        time.sleep(0.2)

# 听音乐
def music():
    for i in range(3):
        print("music...")
        time.sleep(0.2)

if __name__ == "__main__":
    coding_process = threading.Thread(target=coding)
    music_process = threading.Thread(target=music)
    coding_process.start()
    music_process.start()
    