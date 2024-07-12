'''

ZeroDivisionError   当除数为0时，引发的异常
IndexError  索引超出范围所引发的异常
KeyError    字典取值时key不存在的异常
NameError   使用一个没有声明的变量时引发的异常
SyntaxError Python中的语法错误
ValueError  传入的值错误
AttributeError  属性或方法不存的异常
TypeError   类型不合适引发的异常
IndentationError    不正确的缩进引发的异常
'''

#(1)ZeroDivisionError
#print(10/0)

#(2)IndexError
# lst = [10,30,50,90]
# print(lst[4])

#(3)KeyError
# d ={'name':'wenbo','age':18}
# print(d.__getitem__('name'))
# print(d['gender'])

#(4)NameError
# print(hello)

#(5) SyntaxError
# print('hello)

#(6) ValueError
# print(int('a'))  #  这里学到了ord() 和 chr() 方法
print(ord('a'))
# print('love'.encode('utf-8').hex())
# print('love'.hex())    #    AttributeError: 'str' object has no attribute 'hex'   bytes.hex()  bytes 才有的方法


#(7)    AttributeError
# i=10
#print(i.name)

#(8)TypeError
# print('hello'+123)

#(9)IndentationError
    # print('hello world')