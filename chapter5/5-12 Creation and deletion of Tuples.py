"""
元组是不可变类型，没有增删改
元组也是序列 in not in 相加 相乘 len() max() min()  index() count()
"""



# 使用小括号创建元组
t = ('hello',[10,20,30],'python','world')
print(t)

#使用内置函数tuple()创建元组

t = tuple('helloworld')   #把字符串中的每一个元素提取出来，作为元组的每一个元素
print(t)

t = tuple([10,20,30,40])
print(t)

print('10在元组中是否存在：',(10 in t))
print('10在元组中是否存在：',(10 not in t))
print('最大值：',max(t))
print('最小值：',min(t))
print('len：',len(t))
print('t.index()：',t.index(10))
print('t.count()：',t.count(10))

# 如果元组中只有一个元素
t = (10)
print(t,type(t))

# 如果元组中只有一个元素，*** 逗号不能省 ***
y =(10,)
print(y,type(y))

#元组的删除
del t
#print(t)

