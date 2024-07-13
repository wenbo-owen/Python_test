# 个数可变的位置参数

def fun(*para):
    print(type(para))
    for item in para:
        print(item)

fun(10,20,30,40)
fun(10)
fun(20,30)
fun([11,22,33,44])  # 实际上传递的是一个参数

#在调用时候参数前面加一颗星，会将列表进行解包
fun(*[11,22,33,44])  #将列表中的每一个元素 传递给元组中

#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'--->',value)

fun2(name='温博',age=2,key3=3) #关键字参数

d = {'name':'温博','age':18,'height':170}

fun2(**d) #系列解包操作

