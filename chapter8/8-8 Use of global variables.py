a =100 #全局变量

def calc(x,y):
    return a + x +y

print(a)
print(calc(10,20))

print('-'*30)

def calc(x,y):
    a =200  #布局变量，局部变量的名称与全局变量相同
    return a+x+y  #a是局部变量  ， 局部变量的优先级高


print(calc(10,20))
print(a)

print('-'*30)

def calc3(x,y):
    global  s # s是函数中定义的变量，但是使用了global关键字声明，这个变量s成了全局变量
    s = 300  #声明和赋值 必须是分开执行
    return s+x+y

print(calc3(10,20))
print(s)

