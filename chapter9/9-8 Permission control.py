'''
受保护类型：主要供类的内部使用，但不禁止外部访问


'''

class Student():
    #首尾双下划线
    def __init__(self,name,age,gender):
        self._name = name  #self._name 受保护的,只有本类和子类访问
        self.__age = age #self.__age表示私有的,只能类本身去访问
        self.gender = gender #普通的实例属性，类的内部、外部、及子类都可以访问

    def _fun1(self):  #受保护的
        print("子类及本身可以访问")

    def __fun2(self): #私有的 只能类本身去访问
        print('只有定义的类可以访问')

    def show(self): #普通的实例方法
        self._fun1()    #类本身可以访问受保护的方法
        self.__fun2()   #类本身访问私有的方法
        print(self._name) #受保护的属性
        print(self.__age)  #私有的实例属性


#创建一个学生类的对象
stu = Student('温博',20,'女')

#类的外部
print(stu._name)
#AttributeError: 'Student' object has no attribute '__age'. Did you mean: '_name'?
# print(stu.__age) #ERROR

stu._fun1()

# stu.__fun2()  #error
#私有的实例属性和方法是真的不能访问吗？
print(stu._Student__age)  #为什么可以这样访问


stu._Student__fun2()


# dir() 可以以列表的方式 返回所有属性和方法
print(dir(stu)) #['_Student__age', '_Student__fun2' ...