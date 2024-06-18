#Python模块
#如何声明Python变量
#进制转换
#格式化数字
#单行注释和多行注释
#单引号和双引号字符串
#拼接字符串
#长字符串

#Python模块 = 封装了API的Library
# 1.Python自身提供的模块
# 2.自定义的模块
# import
# import module_name
# module_name.function_name   #类似于引用对象的方法

# from module_name import function_name
# function_name

# from module_name import *
# fun1 fun2

import math
print(math.floor(20.8))   #四舍五入函数

from math import sqrt
print(sqrt(20))

from math import *
print(sin(3.14/2))
print(cos(3.14/2))