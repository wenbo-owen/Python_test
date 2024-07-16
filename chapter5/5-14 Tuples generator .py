t =(i for i in range(1,4))
print(t)  # t 是生成器对象
# t = tuple(t)
# print(t)

#遍历
# for item in t:
#     print(item)

print(t.__next__())   #取出第1个元组元素
print(t.__next__())   #取出第2个元组元素
print(t.__next__())   #取出第3个元组元素
t = tuple(t)
print(t)   # 里面没有元素了

