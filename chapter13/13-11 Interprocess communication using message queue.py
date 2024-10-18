from multiprocessing import Process ,Queue
import time
a=100


def write_msg(q):  #q队列
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)   #入队
            print('a入队时的值：',a)

def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('a出队时的值：',q.get())   #出队
         
            

if __name__ == '__main__':
   #父进程开始执行
   print('父进程开始执行')

   #创建消息队列
   q=Queue()  # 队列无上限个数

   p1 = Process(target=write_msg,args=(q,))   #带参数的
   p2 = Process(target=read_msg,args=(q,))

   p1.start()
   p2.start()

   p1.join()
   p2.join() 

   print('父进程结束')