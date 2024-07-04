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

def shuixianhua(num) ->bool:
    units = num % 10
    ten = num // 10 % 10
    hun = num // 100 % 10

    if (units**3 + ten**3 + hun**3) == num :
        print (num,"是水仙花数")
        return True
    else:
        print(num, "不是水仙花数")
        return False


num = input("请输入水仙花数：")
shuixianhua(int(num))