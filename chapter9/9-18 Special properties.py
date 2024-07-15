'''

特殊属性
'''

class A():
    pass

class B():
    pass

class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = A()
b = B()
c = C('wenbo',19)
print('a的属性字典是：',a.__dict__)  #a的属性字典
print('b的属性字典是：',b.__dict__)  #b的属性字典
print('c的属性字典是：',c.__dict__)  #c的属性字典

print('-'*40)
print('对象a的所属的类：',a.__class__)
print('对象b的所属的类：',b.__class__)
print('对象c的所属的类：',c.__class__)

print('-'*40)
print('A类的父类元祖：',A.__bases__)    #类名
print('B类的父类元祖：',B.__bases__)
print('C类的父类元祖：',C.__bases__)

print('-'*40)
print('A的父类',A.__base__)
print('B的父类',B.__base__)
print('C的父类',C.__base__)    #A类 如果继承了N多个父类，结果只显示第一个父类

print('-'*40)
print('A类的层次结构',A.__mro__)
print('B类的层次结构',B.__mro__)
print('C类的层次结构',C.__mro__)  # 自己，继承了A类 B类，间接继承了object类

print('-'*40)

# 子类列表是方法
print('A类的子类列表是：',A.__subclasses__())
print('B类的子类列表是：',B.__subclasses__())
print('C类的子类列表是：',C.__subclasses__())
