from multiprocessing import Process
import os,time 

# 函数式方式创建子进程
def sub_process(name):
    
    print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()}，--------{name}')   # name 是位置参数
    time.sleep(1)

def sub_process2(name):
    print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()}，--------{name}')
    time.sleep(1)

if __name__ == '__main__':

    # 主进程
    print('父进程开始执行')
    # 循环执行5次
    for i in range(5):  
        # 创建第一个子进程
        #p1 = Process()  # 没有给定target参数，不会执行自己编写的函数中的代码，会调用执行Process类中的run方法
        p1 = Process(target=sub_process,args=('wenbo',))  #元组只有一个参数,也需要有逗号
        # 创建第二个子进程
        #p2 = Process()  # 没有给定target参数，不会执行自己编写的函数中的代码，会调用执行Process类中的run方法
        p2 = Process(target=sub_process2,args=('18',))
        # 调用start() 启动子进程

        p1.start()
        p2.start()

        # 终止进程
        p1.terminate()
        p2.terminate()
    
    print('父进程执行完毕')