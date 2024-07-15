class Person(object):
    def __init__(self,name,age):  # 这里相当于方法重写了
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name}，今年我{self.age}岁了')

per =Person('温博',20)
print(per)

# <__main__.Person object at 0x0000020151B318D0>