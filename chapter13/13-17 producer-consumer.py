from queue import Queue
from threading import Thread
import time

# 创建一个生产者类
class Producer(Thread):
    
    def __init__(self, thread_name, queue):
        Thread.__init__(self,name=thread_name)
        self.queue = queue
    def run(self):
       
        for i in range(1,6):
            
            print(f"{self.name}将产品{i}放入了队列")
            self.queue.put(i)
            time.sleep(1)
        print('生产者完成了所有数据的存放')





# 创建一个消费者类
class Consumer(Thread):
    
    def __init__(self, thread_name, queue):
        Thread.__init__(self,name=thread_name)
        self.queue = queue

    def run(self):

        for _ in range(5):
            value = self.queue.get()
            print(f"消费者线程{self.name}取出了{value}")
            time.sleep(1)
        
        print('------消费者完成了所有数据的取出---------')

if __name__ == '__main__':

    # 创建一个队列
    queue = Queue()
    producer = Producer('生产者',queue)
    consumer = Consumer('消费者',queue)

    # 启动线程
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    print('主线程执行完毕')