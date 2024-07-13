'''
    字符串、列表、元组都是可迭代对象
    都可以使用for循环进行遍历操纵

'''

lst = [56,88,14,56,20,1,47]

#lst.sort() # 这种是列表的方法，不是内置函数

#(1) sorted()
asc_lst = sorted(lst)
desc_lst = sorted(lst,reverse=True)
print("源列表",lst)
print("升序",asc_lst)
print("降序",desc_lst)

#(2) reversed() 反向
new_lst = reversed(lst)
print(type(new_lst))  #<class 'list_reverseiterator'>
print(list(new_lst))

#(3) zip
x = ['a','b','c','d']
y = [10,20,30,40,50]
zipobj = zip(x,y)
print(type(zipobj))  #<class 'zip'>
z = list(zipobj)
print('z= ',z)  # [('a', 10), ('b', 20), ('c', 30), ('d', 40)]




#转完后迭代器就空了

print('-'*50)
#(4)
enum = enumerate(y,start=1)
print(type(enum))    #<class 'enumerate'>
print(tuple(enum))  #转完后迭代器就空了
#print(list(enum))

print('-'*50)
#(5) all

lst2 = [10,20,'',30]  #''空字符不是 ' '空格字符
print(all(lst2))
print(all(lst))

print('-'*50)

#（6） any
print(any(lst2))

print('-'*50)

#(7)
zipobj = zip(x,y)
print(next(zipobj))   #next函数的参数只能是 迭代器
print(next(zipobj))

#(8)

print('-'*50)
def fun(num):
    return num%2==1

#将fun结果为True的参数留下来，放到obj中
obj = filter(fun,range(10))  #将range(10) 0-9作用参数，都执行一次fun操作
print(list(obj))  #[1,3,5,7,9]

def Upp(x):
    return x.upper()
new_lst2 = ['hello','world','python']

obj2 = map(Upp,new_lst2)
print(list(obj2))

