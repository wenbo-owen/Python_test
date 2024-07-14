class Student():
    def __init__(self, name,gender):
        self.name = name
        self.__gender = gender  #私有的实例属性
    #使用@property 修改方法，将方法转为属性使用
    @property
    def gender(self):
        return self.__gender

stu = Student('温博','男')
