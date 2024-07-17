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

'''
------------------------增加的内容-------------------------------
关于字典中 迭代器的理解
'''
print('*'*50)
d1 = dict({'温博':36,'王倩':35,'温如水':7})
print(d1)

d1_keys = d1.keys()
d1_values = d1.values()

# print(type(d1_keys),'--->',d1_keys)

# print(dir(d1_keys))
# d2 = d1_keys.__iter__()
# print(dir(d2))
#
# for d1_key in d2:
#     print(d1_key,end='->')

print(type(d1))

print('温博' in d1)
d1['小蝴蝶'] = 18
print(d1)

'''
------------------------增加的内容-------------------------------
对字典类进行重写
'''
print('-'*50)

class Mydict(dict):

    def fun1(self):
        print('兄弟们,这是我重写的一个类！')

md1 = Mydict({'著三岁':36,'小虎队':35,'泡泡龙':7})
print(md1)

for item in md1.items():
    print(item)
md1.fun1()

'''
------------------------增加的内容2024/07/17-------------------------------
对字典类进行重写
'''
class SortedDict(dict):
    class Iterator(object):
        def __init__(self,sorted_dict):
           self._dict = sorted_dict
           self._keys = sorted(self._dict.keys())
           self.nr_items = len(self._keys)
           self._idx = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self._idx > self.nr_items:
                raise StopIteration
            key = self._keys[self._idx]
            value = self._dict[key]
            self._idx += 1
            return key, value

        # __next__ = next

    def __iter__(self):
        return SortedDict.Iterator(self)

    iterkeys = __iter__

new_d1 = {'SA':'小明','CB':'小房','AC':'小值','ED':'小三','MA':'小率'}
print(new_d1)
new_d2 = SortedDict(new_d1)
print(type(new_d2),'-->',new_d2)

for key in new_d2:      #直接遍历SortedDict对象, 不要用打点item方法
    print(key)




#
# d3 = sorted(new_d1)
# for key in d3:
#     print(key,'--->',new_d1[key])

