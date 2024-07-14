import random


def get_max(lst):
    res = lst[0]
    for i in range(len(lst)):
        if lst[i] >= res:
            res = lst[i]

    return res

# lst=[]
# for i in range(1,11):
#     lst.append(random.randint(1,100))

#采用列表声称是
lst = [random.randint(1,100) for i in range(10)]

max = get_max(lst)

print('原列表为：',lst)
print('列表中的最大值为：',max)








# lst = [40,76,28,25,42,17,56,53,43,20,76]
# print('使用内置函数得到的最大值是',max(lst))
#
# res = lst[0]
# for i in range(len(lst)):
#     if lst[i] >= res :
#         res = lst[i]
#
# print('使用非max函数得到的结果是：',res)