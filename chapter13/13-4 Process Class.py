from multiprocessing import Process
import os,time

#自定义一个类

class SubProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        print(f'子进程的PID:{os.getpid()},父进程的PID:{os.getppid()}，--------{self.name}')
        time.sleep(1)

if __name__ == '__main__':
    # 主进程
    print('父进程开始执行')
    lst = []
    # 循环执行5次
    for i in range(1,6):
        # 创建第一个子进程
        p1 = SubProcess('wenbo')
        # 启动进程
        p1.start()
        lst.append(p1)

    for item in lst:
        item.join()

    
    print('父进程执行完毕')