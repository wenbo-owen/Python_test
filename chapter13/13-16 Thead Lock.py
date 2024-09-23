from threading import Thread,Lock
import  threading
import  time

ticket =50 #全局标量 代表50张票
#创建Lock对象
lock_obj=Lock() #多线程共享数据安全问题

def sale_ticket():

    global ticket
    #每个窗口假设有100个人排队
    for i in range(100):
        lock_obj.acquire()
        if ticket > 0:
            
            print(f'{threading.current_thread().name}正在卖第{ticket}张票')
            ticket -=1
        lock_obj.release()
        time.sleep(1)

if  __name__ == '__main__':

    for i in range(3):
        t = Thread(target=sale_ticket)  #多线程共享数据不安全问题 
        t.start()