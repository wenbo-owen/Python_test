#创建空集合
s = set()

# 录入5位好友的姓名和手机号
for i in range(6):
    info = input(f'请输入第{i}位还有的姓名和手机号:')
    #添加到集合中
    s.add(info)

#遍历集合
for item in s:
    print(item)