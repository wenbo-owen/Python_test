#编写一个person 类型
# 类相当于图纸，只有创建对象后才能使用

class Person():
    pass

class Cat():
    pass

class Dog:
    pass

class Student:
    pass

#创建类的对象
# 对象名 = 类名()

per = Person()
c = Cat()
d = Dog()
stu = Student()

print(type(per))  #<class '__main__.Person'>
print(type(c))
print(type(d))
print(type(stu))
