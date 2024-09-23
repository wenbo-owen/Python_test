'''
在这段代码中，join起到的作用是：等待被调用的线程执行结束。
具体来说，当在主线程中对一个线程对象调用join方法时，主线程会被阻塞，直到被调用的线程执行完毕。
在这段代码中，对于每个创建的线程，在启动后又调用了join方法，
这意味着主线程会等待所有创建的两个线程都执行完任务后才继续往下执行。
这样做的好处是可以确保主线程在所有子线程完成任务后，再进行后续的操作，保证程序按照预期的顺序执行，
避免出现数据不一致或资源竞争等问题。同时，通过计算程序开始时间start = time.time()和最后所有线程执行完毕后的时间差，
可以方便地测量多线程执行任务的总时间。
'''


import threading
from threading import Thread
import time 

#编写函数
def test():
    for i in range(3):
        time.sleep(1)
        print(f'线程：{threading.current_thread().name}正在执行{i}')

if __name__ == '__main__':

    #创建线程
    start = time.time()
    lst = [Thread(target=test) for i in range(2)]

    for item in lst:
        item.start()

    # for item in lst:
    #     item.join()

    print("运行的时间是：",time.time()-start)