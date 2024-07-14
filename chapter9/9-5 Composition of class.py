'''
    类的组成
    类属性  类方法 静态方法都是使用类名去调用的
    跟实例有关的都是使用对象名打点调用的

'''

class Student():

    #类属性，定义在类中，方法外的变量
    school = '北京xxx教育'

    # name,age 是方法的参数,是局部表变量,name，age的作用域是整个__init__方法
    def __init__(self,name,age):
        self.name = name  #左侧是实例属性,name是局部变量，将局部变量name的值赋值给实录属性self.name
        self.age = age   #实例属性的名称 和 局部变量的名称可以相同

    #定义在类中的函数，成为方法，自带一个self参数
    def show(self):
        print(f'我叫：{self.name}，今年：{self.age}岁了')

    #静态方法
    @staticmethod
    def sm():
        # print(self.name)    #ERROR
        # print(self.show())  #ERROR
        print('这是一个静态方法，不能调用实例属性，也不能调用实例方法')
    #类方法
    @classmethod
    def cm(cls):   #cls --> class的缩写
        print('这是一个类方法，也不能调用实例属性，也不能调用实例方法')




# 创建类的对象

#为什么传了2个参数，因为__init__方法中有2个形参.self是自带的参数，无需手动传入
stu = Student('wenbo',18 )


#实例属性，使用对象名进行打点调用
print(stu.name,stu.age)

#类属性, 直接使用类名，打点调用
print(Student.school)

#实例方法,使用对象名进行打点调用
stu.show()

#类方法，@classmethod进行修饰的方法,直接使用类名打点调用
Student.cm()

#静态方法，@staticmethod进行修饰的方法,直接使用类名打点调用
Student.sm()


