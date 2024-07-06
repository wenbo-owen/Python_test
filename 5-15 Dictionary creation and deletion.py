#(1) 创建字典
d= {10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d)  #key相同时，value进行了覆盖

#(2) zip函数
lst1 = [10,20,30,40]
lst2 = ['cat','dog','pet','zoo','car']
zipobj = zip(lst1,lst2)  # 映射对象 需要转换成其他类型
print(zipobj)  #<zip object at 0x00000152AD52FE40>

# print(list(zipobj))
d = dict(zipobj)
print(d)

#使用参数创建字典
d = dict(cat=10,dog=20)  #cat是键 ,右侧是value
print(d)

t=(10,20,30)
print({t:10})  # t是key ,10是value，元组是可以作为字典中的key的

#列表是不可以作为字典中的键的
# lst = [10,20,30]
# print({lst:10})     #TypeError: unhashable type: 'list'

#字典属于序列  内置方法
print('max',max(d))
print('min',min(d))
print('len',len(d))

#字典的删除
del d
# print(d)
