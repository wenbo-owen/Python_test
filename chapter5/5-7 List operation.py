"""
可变数据类型，元素长度内容可变，但是地址不变
    lst.append(x)   在列表Ist最后增加一个元素
    lst.insert(index,x) 在列表中第index位置增加一个元素
    lst.clear()     清除列表Ist中所有元素
    lst.pop(index)  将列表Ist中第index位置的元素取出，并从列表中将其删除
    lst.remove(x)   将列表Ist中出现的第一个元素x删除
    lst.reverse(x)  将列表Ist中的元素反转
    lst.copy()      拷贝列表Ist中的所有元素，生成一个新的列表
"""

lst =['hello','world','python']
print('原列表',lst,id(lst))  #id() 输出内存地址

# 增加元素操作
lst.append('sql')
print('增加元素之后的列表',lst,id(lst))  #id() 输出内存地址

#使用insert(index,x)在指定index位置插入元素x
lst.insert(1,100)
print(lst)

#列表元素的删除操作
lst.remove('world')
print('删除元素之后的列表',lst,id(lst))  #id() 输出内存地址

#使用pop(index)根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

#清除列表中所有元素
# lst.clear()
# print(lst,id(lst))

#列表的反向
lst.reverse()   #不会产生新的列表，在原列表基础上进行反向
print(lst)

# 列表的拷贝，将产生一个新的列表对象
new_list = lst.copy()
print('new_list',new_list,id(new_list))

#列表元素的修改
#根据索引进行修改
lst[1] = 'mysql'
print(lst )



