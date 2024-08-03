import admin.my_admin as a  #包名.模块名 admin是包名，my_admin是模块名

a.info_hello()
print('-'*40)

from admin import my_admin as b     #from 包名 import 模块 as 别名

b.info_hello()
print('-'*40)

from admin.my_admin import info_hello  #from 包名.模块名 import 函数/变量

info_hello()
print('-'*40)

from admin.my_admin import *

info_hello()
print('-'*40)
print(name)