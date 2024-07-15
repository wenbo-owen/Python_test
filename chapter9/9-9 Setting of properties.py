class Student():
    def __init__(self, name,gender):
        self.name = name
        self.__gender = gender  #私有的实例属性
    #使用@property 修改方法，将方法转为属性使用
    @property
    def gender(self):   #取值操作
        return self.__gender

    # 将我们的gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value): #赋值操作
        if value not in ['Male','Female']:
            print('性别有误，已将性别默认设置为男')
            self.__gender = '男'
        else:
            self.__gender = value


stu = Student('温博','男')
print(stu.name,'的性别是：',stu.gender)      #stu.gender就会去执行stu.gender()


#尝试修改属性值
#AttributeError: property 'gender' of 'Student' object has no setter
#stu.gender = '女'

print('-'*50)
stu.gender = '其他'