from multiprocessing import Pool
import os,time

#编写任务
def task(name):
    print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()}，--------{name}')
    time.sleep(1)


if __name__ == '__main__':

    start = time.time()     # 获取时间戳
    # 主进程
    print('父进程开始执行')
    #创建进程池
    p = Pool(3)

    #创建任务
    for i in range(10):
        #以阻塞的方式
        p.apply(task,args=(i,))   # 任务一个一个出来  时间戳10.361729145050049

    p.close()   # 关闭进程池，不再接受新的进程
    p.join()    #  阻塞父进程 等待所有子进程执行完毕
    print('所有的子进程执行完毕，父进程执行结束')


    print(time.time()-start)
     




