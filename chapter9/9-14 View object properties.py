class Person(object):
    def __init__(self,name,age):  # 这里相当于方法重写了
        self.name = name
        self.age = age

    def show(self):
        print(f'大家好，我叫{self.name}，今年我{self.age}岁了')

per =Person('温博',20)
per.show()

print(dir(per))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
 '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
 '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
 '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 
 '__weakref__', 'age', 'name', 'show'
 ]

'''