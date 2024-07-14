'''
类属性和实例属性

'''

class Student():

    #类属性，定义在类中，方法外的变量
    school = '北京xxx教育'

    # name,age 是方法的参数,是局部表变量,name，age的作用域是整个__init__方法
    def __init__(self,name,age):
        self.name = name  #左侧是实例属性,name是局部变量，将局部变量name的值赋值给实录属性self.name
        self.age = age   #实例属性的名称 和 局部变量的名称可以相同
