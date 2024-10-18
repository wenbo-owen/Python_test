lst=['helloo','world','98','100.5']
print(lst)

#可以使用内置函数list()创建列表
lst2 = list('i love mg')
print(lst2)

lst3 = list(range(1,10,2)) #从1-10 步长为2
print(lst3)

#列表是序列中的一种，对序列的操作符、运算符，函数均可使用
print(lst + lst2 + lst3)
lst1 = lst + lst2 + lst3
print(lst1*3)
print(len(lst3))
print(max(lst3))
print(min(lst3))

print('-'*30)
print(f'list1 is {lst1}')
print(f'he在列表中出现了{lst1.count("he")}次') 
print(f'world在列表中出现了{lst1.count("world")}次') # 如果采用f''的话，''内部需要调用字符串用双引号""
print(f'o在lst1中的索引是{lst1.index("o")}')


#列表的删除操作
lst4=[10,20,30]
#删除列表操作
print(lst4)
del lst4
#print(lst4)


