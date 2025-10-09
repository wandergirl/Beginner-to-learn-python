"""

        线程:实现多任务的另一种形式，线程是程序执行的最小单位一个进程最小一个线程执行程序
        线程的作用：多线程执行多任务，提高执行效率
        线程执行带有参数的使用 :
                            # target:线程执行的函数名
                            # args:表示以元组的方式给函数传参
"""
import multiprocessing


def YUUKA():
    for i in range(4):
        print("财政+1......")
def AL1S():
    for i in range(4):
        print("财政-1......")
# 1.导入线程模块
import threading
#通过线程类创建线程对象 线程对象 = threading.Thread(target = 任务名)
thread = threading.current_thread()

if __name__ == "__main__":
    yuuka = threading.Thread(target=YUUKA).start()
    al1s = threading.Thread(target=AL1S).start()
