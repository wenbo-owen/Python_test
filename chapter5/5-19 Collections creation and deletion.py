#{}直接创建集合
s = {10,20,30,40}
print(s)

# 集合只能存储不可变数据类型
#s = {[10,20],[30,40]} #unhashable type: 'list'  hash就是无序的

# 使用set创建一个集合
s = set()  #创建一个空集合，空集合的布尔值是False
print(s)
s ={}
print(s,type(s)) #dict

s = set('helloworld')
print(s)

s2 = set([10,20,30])
print(s2)

s3 = set(range(1,10))
print(s3)

#集合属于序列中的一种
print('max:',max(s3))
print('min:',min(s3))
print('len:',len(s3))

print('9在集合当中存在吗', (9 in s3))
print('9在集合当中不存在吗', (9 not in s3))

#集合的删除操作
del s3
#print(s3) #NameError: name 's3' is not defined. Did you mean: 's'?

