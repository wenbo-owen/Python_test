s = 'helloworld'
print('e在hello_world中存在吗？','e'in s)
print('v在hello_world中存在吗？','v'in s)
print('e在wenbo中存在吗？','e'in 'wenbo')
print('e在wenbo中存在吗？'+str('e' in 'wenbo'))


print('-'*40)
#not in 的
print('e在hello_world中不存在吗？','e'not in s)
print('v在hello_world中不存在吗？','v'not in s)
print('-'*40)

#内置函数的使用
print('len():',len(s))
print('max():',max(s))
print('min():',min(s))

#序列对象的相关方法，使用序列的名称，打点调用
print('s.index()',s.index('o'))
#报错了
#print('s.index()',s.index('v'))

#统计'o'的个数
print('s.count()',s.count('o'))