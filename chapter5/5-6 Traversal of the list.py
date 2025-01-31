"""
    示例5-6 列表的遍历操作
    列表是我们学习的第一个可变数据类型
    具有 增、删、改、查这样的方法


"""

#2025/1/31 复习一次

# 第一种
lst = ['hello', 'world', 'python','php']

for item in lst:
    print(item)     #print(item,end=' ')


print('-'*30)
#第二种 使用for循环，range()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'--->',lst[i])

print('-'*30)
#第三种遍历方式 使用enumerate()函数
for index,item in enumerate(lst):
    print(index,item)  #index是序号 不是索引

print('-'*30)
#手动修改序号的起始值
for index,item in enumerate(lst,start=1):
    print(index, item)

print('-'*30)
for index,item in enumerate(lst,1):  # start= 可以省略
    print(index, item)