'''
只有一句函数体的函数可以使用匿名函数(lambda)

'''

def calc(a,b):
    return a+b

print(calc(10,20))

#匿名函数
s= lambda a,b:a+b    #s 表示一个匿名函数

print(type(s))  # <class 'function'>

#调用匿名函数
print(s(10,20))

print('-'*50)

#列表的正常取值操作
lst = [1,2,3,4,5]
for item in range(len(lst)):
    print(lst[item])
print()

print('*********分隔一下**********')

for item in range(len(lst)):
    result = lambda x:x[item] #根据索引取值，result的类型是function
    print(result(lst))  #lst是 实际参数
print()

#
student_score = [

    {'name':'John', 'score':98},
    {'name': 'tim', 'score': 100},
    {'name': 'owen', 'score': 66},
    {'name': 'wany', 'score': 55},
]
#对列表进行排序,排序的规则是字典中的成绩
#key是排序的规则
#student_score.sort(key=lambda x:x['score'])
student_score.sort(key=lambda x:x.get('score'),reverse=True) #降序

print(student_score)