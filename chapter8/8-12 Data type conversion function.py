print('非空字符串的布尔值：',bool('hello'))   #True
print('空字符串的布尔值：',bool('')) # 空字符串不是空格字符中
print('空列表的布尔值：',bool(list()))
print('空元组的布尔值：',bool(()))
print('空元组的布尔值：',bool(tuple()))
print('空集合的布尔值：',bool(set()))
print('空字典的布尔值：',bool({}))
print('空字典的布尔值：',bool(dict()))

print('-'*50)

print('非0数值型的布尔值:',bool(123))
print('整数0的布尔值：',bool(0))
print('浮点数0.0的布尔值:',bool(0.0))

print('-'*50)

#将其他类型转换成字符串
lst=[10,20,30]
print(type(lst),lst)

s = str(lst)
print(type(s),s)  # 确实变成了一个字符串 ’[10, 20, 30]‘

print('-'*50)

# float类型和str类型 转成int 类型
print('-'*30,'float类型和str类型转成int类型','-'*30)
print(int(98.7) + int('50'))

#注意事项
#ValueError: invalid literal for int() with base 10: '98.7'
# print(int('98.7')) #错误

#ValueError: invalid literal for int() with base 10: 'a'
#print(int('a'))  #错误

print('-'*30,'int类型和str类型转成float类型','-'*30)
print(float(90)+float('3.14'))

s ='hello'
print(list(s))

seq = range(1,10)
print(tuple(seq))