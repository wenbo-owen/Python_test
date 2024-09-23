from multiprocessing import Queue

if __name__ == '__main__':
    #创建一个队列
    q = Queue(3) #最多可以接收3条信息
   
    #向队列中添加信息
    q.put('hello')
    q.put('world')
    q.put('python')

    q.put('html',block=True,timeout=2)