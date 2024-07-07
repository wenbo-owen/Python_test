d = {1001:'温博',1002:'王倩',1003:'温如水'}
print(d)

# 向字典中添加元素
d[1004] = '妈妈'  # 直接使用赋值运算符向字典中添加元素
print(d)

# 获取字典中所有的key
keys = d.keys()
print(keys)   # dict_keys([1001, 1002, 1003, 1004]) 对象
print(list(keys))
print(tuple(keys))

# 获取字典中所有的value
values = d.values()
print(values) #dict_values(['温博', '王倩', '温如水', '妈妈'])
print(list(values))
print(tuple(values))

#如何将字典中的数据转成key-value的形式，以元组的方式进行展现
lst = list(d.items())
print(lst)

# list 转换为 字典
d = dict(lst)
print(d)

# 使用pop 函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在的'))

#随机删除
print(d.popitem())
print(d)

# d.clear()
# print(d)
print(bool(d))