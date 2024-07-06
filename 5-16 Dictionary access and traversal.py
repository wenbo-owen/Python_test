"""
字典元素的访问和遍历

"""
#访问字典中的元素
#(1) 使用d[key]
d = {'hello':10,'world':20,'python':30}
print(d['hello'])

#(2) d.get(key)
print(d.get('python'))
# 二者之间是有区别的，如果key不存在,d[key]报错，d.get(key)可以指定默认值
print(d.get('java'))
print(d.get('java','不存在'))

#字典的遍历
for item in d.items():
    print(item)   #key=value 组成一个元素

#在使用for循环遍历时，分别获取key,value
for key,value in d.items():
    print(key,'--->',value)
