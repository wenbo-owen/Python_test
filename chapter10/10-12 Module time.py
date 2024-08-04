'''

time模块
time模块是Python中提供的用于处理时间的标准库,可以用来进行时间处理、时间格式化和计时等

time()    获取当前时间戳
localtime(sec)    获取指定时间戳对应的本地时间的struct_time对象
ctime()    获取当前时间戳对应的易读字符串
strftime()    格式化时间，结果为字符串
strptime()    提取字符串的时间，结果为struct_time对象
sleep(sec)    休眠sec秒

'''

import time

now = time.time()       #时间戳
print(now)

obj = time.localtime() #struct_time 对象
print(obj)


obj2 = time.localtime(60)  #60秒 1970年 1月1日，8时，1分，0秒

print(obj2)
print(type(obj2))
print('年份：',obj2.tm_year)
print('月份：',obj2.tm_mon)
print('日期：',obj2.tm_mday)
print('时间：',obj2.tm_hour)
print('分：',obj2.tm_min)
print('秒：',obj2.tm_sec)
print('星期：',obj2.tm_wday)  # [0.6]  3表示星期四
print('今年的多少天',obj2.tm_yday)
print(time.ctime())         #Sun Aug  4 07:50:34 2024

print('-'*40)
# 日期时间格式化
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))  #str--字符串 ->format --time时间
print('%B月份的名称',time.strftime('%B',time.localtime()))
print('%A月份的名称',time.strftime('%A',time.localtime()))

# 字符串转成 struct_time
print(time.strptime('2008-08-08','%Y-%m-%d'))

time.sleep(20)#
print('hello world')