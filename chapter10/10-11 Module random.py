'''
random模块是Python中用于产生随机数的标准库

seed(x)  初始化给定的随机数种子，默认为当前系统时间
random() 产生一个[0.0,1.0)之间的随机小数
randint(a,b) 生成一个[a,b]之间的整数
randrange(m,n,k) 生成一个[m,n)之间步长为k的随机整数
uniform(a,b) 生成一个[a,b]之间的随机小数
choice(seq) 从序列中随机选择一个元素
shuffle(seq) 将序列seq中元素随机排列，返回打乱后的序列
'''
import random

#设置随机数的种子
random.seed(10)
print(random.random())    # random() -> x in the interval [0, 1)
print(random.random())

print('-'*40)
random.seed(10)
print(random.randint(1,100))   #eturn random integer in range [a, b], including both end points.

print('-'*40)
for i in range(10): #[m,n)步长为k ,m-->start-->1 ,n-->stop-->10,k->step-->3
    print(random.randrange(1,10,3))  #12行代码执行10次

print(random.uniform(1,100)) #[a,b] 随机小数

print('-'*40)

lst = [i for i in range(1,11)]
print(random.choice(lst))

#随机的排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)

