#(1) 方法1 import模块
import my_info

#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'info', 'name']
#print(dir(my_info))

print(my_info.name)
my_info.info()
print('-'*50)
#给模块起个别名

# (2)from...import
from my_info import name
print(name)   #导入的是一个具体的变量名称
#info()

from my_info import info
info()

# 通配符
from my_info import *
print(name)
info()

# 同时导入多个模块
import time,math,random