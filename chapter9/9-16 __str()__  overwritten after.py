class Person(object):
    def __init__(self,name,age):  # 这里相当于方法重写了
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name}，今年我{self.age}岁了')

    def __str__(self):
        #return super().__str__() + ' 我重写了 '
        return '这是一个人类，具有name和age'  # 返回值是一个字符串

per =Person('温博',20)
print(per)            #还是内存地址吗？不是，__str__方法中的内容 直接输出对象名，实际上是调用__str__方法
print(per.__str__())

# <__main__.Person object at 0x0000020151B318D0>