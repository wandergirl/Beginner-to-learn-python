"""
        进程介绍: 进程是资源分配的自小单位，它是操作系统进行资源分配和调度运行的基本单位，通俗理解：一个正在运行的程序就是一个进程
        多进程的作用:
        创建进程类创建进程对象 : 进程对象 = multiprocessing.process(target=任务名)
        注：主进程会等待所有子进程执行结束后在结束，守护进程主进程结束子进程自动销毁不在执行

"""
import multiprocessing
import time
from os import getpid,getppid
from multiprocessing import Process
def sing(num):
    print("唱歌进程的pid：",getpid())
    for i in range(3):
        num =i
        print(f"唱歌。。。。{i}次")
        time.sleep(0.5)
def dance(num):
    print("跳舞的pid:",getpid())
    for i in range(3):
        print(f"跳舞。。。。{i}次")
        time.sleep(0.5)
"""
                获取进程的编号:
                            1.获取当前进程编号
                            import os 
                            os.getpid()
                            2.获取当前父进程编号
                            os.getppid()
"""
def YUUKA():
    print("YUUKA的pid:",getpid())
    print("YUUKA的ppid:",getppid())
    print("财政+1.....")
def AL1S():
    print("AL1S的pid:", getpid())
    print("AL1S的ppid:", getppid())
    print("财政-1")
#

if __name__ == '__main__':
   # sing_process = multiprocessing.Process(target=sing).start() # target指定进程对象
   # dance_process = multiprocessing.Process(target=dance).start()
    """
                进程执行带有参数的任务:
                                   
                                   target: 表示进程执行的函数名
                                   args: 表示以元组的方式给函数传参
                                   sing_process =multiprocessing.Process(target=sing,args = (3,))
                                   kwargs: 参数的使用以字典的方式给函数传参
                                   sing_process =multiprocessing.Process(target=sing,args = {"num":3})
                                   
    """

    yuuka = multiprocessing.Process(target=YUUKA).start()
    al1s = multiprocessing.Process(target=AL1S).start()
    sing_process = multiprocessing.Process(target=sing,args=(4,)).start()
    dance_process = multiprocessing.Process(target=dance,args=(4,)).start()


    yuuka = multiprocessing.Process(target=YUUKA).start()
    AL1S_1 = multiprocessing.Process(target=AL1S).start()






