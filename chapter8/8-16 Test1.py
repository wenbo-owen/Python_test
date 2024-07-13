lst = [40,76,28,25,42,17,56,53,43,20,76]
print('使用内置函数得到的最大值是',max(lst))

res = lst[0]
for i in range(len(lst)):
    if lst[i] >= res :
        res = lst[i]

print('使用非max函数得到的结果是：',res)