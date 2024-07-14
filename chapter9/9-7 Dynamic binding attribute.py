class Student():

    #类属性，定义在类中，方法外的变量
    school = '北京xxx教育'

    # name,age 是方法的参数,是局部表变量,name，age的作用域是整个__init__方法
    def __init__(self,name,age):
        self.name = name  #左侧是实例属性,name是局部变量，将局部变量name的值赋值给实录属性self.name
        self.age = age   #实例属性的名称 和 局部变量的名称可以相同

    #定义在类中的函数，称为方法，自带一个self参数 (实例方法)
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

stu = Student('wenbo',20)
stu2 = Student('wrs',9)
print(stu.name,stu.age)
print(stu2.name,stu2.age)

# 为stu2动态绑定一个实例属性
stu2.gender = '小孩'      # stu2所独有的
print(stu2.name,stu2.age,stu2.gender)
# print(stu.gender)   #ERROR

#动态绑定方法
def introduce():
   print('我是一个普通函数，我被动态绑定成了stu2对象的方法')

stu2.fun = introduce  # 这里是赋值 ，  不要加()， 加()就是函数的调用了
stu2.fun()