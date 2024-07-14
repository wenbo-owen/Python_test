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


# 根据“图纸可以创建N多个对象”
stu = Student('wenbo',18)
stu2 = Student('wenrushui',18)
stu3 = Student('wangqian',1)
stu4 = Student('yesok',58)

print(type(stu))

Student.school = '你好世界' #给类的类属性赋值

#将学生对象存储在列表中
lst =[stu,stu2,stu3,stu4]

for item in lst:
    item.show()

print('-'*50)

print(format(id(stu),'x'))
print(id(stu2))