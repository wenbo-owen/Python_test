"""
列表的排序操作
1）列表对象的sort方法
Ist.sort(key=None,reverse=False)
key：表示排序的规则
reverse：表示排序方式（默认升序）


"""

lst = [4,56,3,78,40,56,89]
print('原列表',lst)

#排序，默认是升序
lst.sort() #排序是在原列表的基础上，不会产生新的列表对象
print('升序',lst)

lst.sort(reverse=True)
print('降序',lst)
print('-'*40)

lst2 = ['banana','apple','Cat','Orange']
print('原列表',lst2)
#升序排序，先排大写，再排小写
lst2.sort()
print('升序',lst2)

lst2.sort(reverse=True)
print('降序',lst2)
print('-'*40)

#忽略大小写进行比较
lst2.sort(key=str.lower)  #参数不加括号，调用才加括号
print(lst2)