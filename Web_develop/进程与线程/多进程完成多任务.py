# 导入进程模块
import multiprocessing
import time
import os

# 编写函数
def coding():
    print("coding>>>%d" % os.getpid())
    print("coding父进程>>>%d" % os.getppid())
    for i in range(3):
        print("coding...")
        time.sleep(0.2)

# 听音乐
def music():
    print("music>>>%d" % os.getpid())
    print("music父进程>>>%d" % os.getppid())
    for i in range(3):
        print("music...")
        time.sleep(0.2)

if __name__ == "__main__":
    print("主进程>>>%d" % os.getpid())
    coding_process = multiprocessing.Process(target=coding)
    music_process = multiprocessing.Process(target=music)
    coding_process.start()
    music_process.start()
    