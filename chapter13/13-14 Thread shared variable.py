from threading import Thread

a=100 #全局变量
def add():
    print('加线程开始')
    global a
    a+=30
    print(f'a={a}')
    print('加线程结束')

def sub():
    print('减线程开始')
    global a
    a-=50
    print(f'a={a}')
    print('减线程结束')

if __name__ == '__main__':
    #主进程
    print('主线程开始执行')
    print(f'------a={a}-------')
    add = Thread(target=add)
    sub = Thread(target=sub)
    add.start()
    sub.start()

    add.join()
    sub.join()
    print('主线程执行完毕')