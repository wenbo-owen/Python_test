'''
方法重写
子类继承了父类就拥有了父类中公有成员和受保护的成员
父类的方法法并不能完全适合子类的需要求
这个时候子类就可以重写父类的方法
子类在重新父类的方法时，要求方法的名称必须与父类方法的名称相同，
在子类重写后的方法中可以通过super().xxx()调用父类中的方法
'''

class Person():  #默认继承了object
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f'大家好，我叫{self.name}，我今年：{self.age}岁')


#Student类继承Person类
class Student(Person):
    def __init__(self,name,age,stuno):  #编写初始化方法
        super().__init__(name,age)      #调用父类的初始化方法
        self.stuno = stuno

    def show(self):
        #调用父类中的方法
        super().show()
        print(f'我来自xx大学，我的学号是：{self.stuno}')

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

    def show(self):
        #super().show()
        print(f'我叫{self.name}，我今年{self.age}岁，我工作的科室是{self.department}')




#创建第一个子类对象
stu = Student('陈美美',20,1001)
stu.show()  #调用子类自己的show方法

doctor = Doctor('小蝴蝶',28,'内科')
doctor.show()