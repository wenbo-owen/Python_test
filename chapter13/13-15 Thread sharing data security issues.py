from threading import Thread
import  threading
import  time

ticket =50 #全局标量 代表50张票

def sale_ticket():

    global ticket
    #每个窗口假设有100个人排队
    for i in range(100):
        if ticket > 0:
            
            print(f'{threading.current_thread().name}正在卖第{ticket}张票')
            ticket -=1
        time.sleep(1)

if  __name__ == '__main__':

    for i in range(2):
        t = Thread(target=sale_ticket)
        t.start()