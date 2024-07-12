s1 = 'hello'
s2 = 'world'
print(s1 + s2)

print('-'*50)
#(2)使用字符串的join()方法

print(''.join([s1,s2])) #helloworld
print('*'.join(['hello','world','python','world','php'])) # hello*world*python*world*php
# hello你好world你好python你好world你好php
print('你好'.join(['hello','world','python','world','php']))


#(3) 直接拼接

print('hello''world')

#(4) 使用格式化字符串进行拼接
print('%s%s' %(s1,s2))   #元组
print('{0}{1}'.format(s1,s2))
