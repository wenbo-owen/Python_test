'''
datetime.datetime   表示日期时间的类

'''

from datetime import datetime

dt= datetime.now()
print('当前的系统时间为：',dt)

# datetime 是一个类，手动创建这个类的对象
dt2 = datetime(2028,8,8,20,8)
print('dt2的数据类型',type(dt2),'dt2所表示的日期时间：',dt2)

print('年：',dt2.year,'月：',dt2.month,'日：',dt2.day)
print('时：',dt2.hour,'分：',dt2.minute,'秒：',dt2.second)

# 比较两个datatime 类型对象的大小

labor_day = datetime(2028,5,1,0,0,0)
national_day = datetime(2028,10,1,0,0,0)

print('2028年5月1日比2028年10月1日早吗？',labor_day<national_day)

#datatime 类型与字符串进行转换
nowdt = datetime.now()
print('nowdt的数据类型是什么:',type(nowdt) ,'nowdt所表示的数据是什么', nowdt)
nowdt_str = nowdt.strftime('%Y/%m/%d %H:%M:%S')
print('nowdt_str的数据类型是什么:',type(nowdt_str) ,'nowdt_str所表示的数据是什么', nowdt_str)

#字符串类型转成datetime类型
str_datetime = '2028年8月8日 20点8分'
dt3 = datetime.strptime(str_datetime,'%Y年%m月%d日 %H点%M分')
print('str_datetime的数据类型是什么:',type(str_datetime) ,'str_datetime所表示的数据是什么', str_datetime)
print('dt3的数据类型是什么:',type(dt3) ,'dt3所表示的数据是什么', dt3)