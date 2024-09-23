from multiprocessing import Queue

if __name__ == '__main__':
    #创建一个队列
    q = Queue(3) #最多可以接收3条信息
    print('队列是否为空：',q.empty())
    print('队列是否为满：',q.full())
    print('-'*40)

    #向队列中添加信息
    q.put('hello')
    q.put('world')
    print('队列是否为空：',q.empty())   #False
    print('队列是否为满：',q.full())    #False
    print('-'*40)

    q.put('Python')
    print('队列是否为空：',q.empty())   #False
    print('队列是否为满：',q.full())    #True
    print('队列当中信息的个数是：',q.qsize())
    print('-'*40)

    # 出队
    print(q.get())
    print('队列中信息的个数：',q.qsize())   
    q.put_nowait('html')
    #q.put_nowait('sql')     # 报错queue.Full
    #q.put('sql')             # 不报错 程序一直在等待，什么时候有出队，再进行一次入队
    print('-'*40)
    
    #遍历
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait())   #nowait() 不等待
    
    print('队列是否为空：',q.empty())   #True
    print('队列是否为满：',q.full())
    print('队列当中信息的个数是：',q.qsize())