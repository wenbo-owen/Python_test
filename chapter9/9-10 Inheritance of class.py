'''
继承了就拥有 父类的公有的和受保护的成员

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

class Doctor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

#创建第一个子类对象
stu = Student('陈美美',20,1001)
stu.show()

doctor = Doctor('小蝴蝶',28,'内科')
doctor.show()
