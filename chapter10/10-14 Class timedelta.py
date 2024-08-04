'''

datetime.timedelta 表示时间间隔的类
不能做年和月的加减
'''

from datetime import datetime
from datetime import timedelta

#创建2个datetime类的对象

delta1 = datetime(2028,10,1) - datetime(2028,5,1)
print('delta1的数据类型是什么 ', type(delta1),'--->','delta1所表示的数据是:',delta1)
print('2028年5月1日之后的153天是那天？',datetime(2028,5,1)+delta1)

#通过传入参数的方式创建一个timedelta对象
td1 = timedelta(10)
print('创建一个10天的timedelta对象',td1)

td2 = timedelta(10,11)
print('创建一个10天的timedelta对象',td2)

td3 = timedelta(days=20,hours=10,minutes=20)
print(td3)