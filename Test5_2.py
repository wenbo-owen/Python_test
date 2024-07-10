#创建一个空列表，用于存储入库的商品信息
lst=[]
lst2=[]
for i in range(5):
    goods= input('请输入商品的编号和商品的名称进行商品入库，每次只能输入一件商品：')
    lst.append(goods)

# 输出所有的商品信息
for item in lst:
    print(item)


while True:
    gou = input('请输入要购买的商品编号：')
    flag = False
    for item in lst:
        if item[0:4] == gou:                        # 切片操作
            print(item[0:4])
            print('商品已成功添加购物车')
            lst2.append(item)
            flag = True
            break                                   #跳出for

    if flag == False and gou != 'q':
            print('商品不存在1')

    if gou == 'q' :
            break                   #退出while循环

lst2.reverse()

print('-'*50)
print('您购物车里已选择的商品为：')
for i in lst2:
    print(i)