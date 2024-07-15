#赋值

class Cpu():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk


cpu = Cpu()
disk = Disk()
computer = Computer(cpu,disk)

#变量对象的复制
computer1 = computer


print(computer,'子对象的地址是：',computer.cpu,computer.disk)
print(computer1,'子对象的地址是：',computer1.cpu,computer1.disk)

print('-'*50)

'''
 浅拷贝：拷贝时，对象包含的子对象内容不拷贝，因此源对象于拷贝对象会引用同一个子对象
'''

import copy

computer2 = copy.copy(computer) #浅拷贝

print(computer,'子对象的地址是：',computer.cpu,computer.disk)
# computer2是新产生的对象，其子对象cpu和disk不变
print(computer2,'子对象的地址是：',computer2.cpu,computer2.disk)

print('-'*50)
'''
深拷贝：
'''

computer3 = copy.deepcopy(computer) #深拷贝

print(computer,'子对象的地址是：',computer.cpu,computer.disk)
# computer3是新产生的对象，其子对象cpu和disk重新创建
print(computer3,'子对象的地址是：',computer3.cpu,computer3.disk)