'''

实现水仙花数
'''

for i in range(1,1000):
    units = i%10
    hun = i // 100
    ten = i//10%10

    if (units**3 + ten**3 + hun**3) == i :
        print (i,"是水仙花数")
else:
    print("计算结束")