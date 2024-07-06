'''
列表的排序  内置方法
2）内置函数sorted()
sorted(iterable,key=None,reverse=False)
表示的是排序的对象


'''
lst = [4,56,3,78,40,56,89]

asc_lst = sorted(lst)
print('升序',asc_lst,id(asc_lst))

desc_lst = sorted(lst,reverse=True)
print('降序',desc_lst,id(desc_lst))

print('原列表',lst,id(lst))

lst2 = ['banana','apple','Cat','Orange']
print('原列表',lst2)

new_lst2 = sorted(lst2,key= str.lower)
print(new_lst2)
