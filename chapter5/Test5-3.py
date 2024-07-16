#创建字典用于存储车票信息.
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','18:19',"00:59"],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}

print('车次   出发站-到达站     出发时间    到达时间    历时时长')

#遍历字典中的元素
for key in dict_ticket.keys():
    print(key ,end='  ')
    for item in dict_ticket.get(key):
        print(item,end='\t\t')
    #换行
    print()

# 输入用户的购票车次
train_no = input('请输入要购买的车次:')

info = dict_ticket.get(train_no)

if info!='车次不存在':
    person = input('请输入乘车人，如果是多为乘车人使用逗号隔开:' )

    s = info[0] +' '+info[1]+'开'
    print('您已购买了'+train_no + ' '+s +',请'+person+'尽快换取纸质车票 【铁路客服】')
else:
    print('您购买的车次不存在')