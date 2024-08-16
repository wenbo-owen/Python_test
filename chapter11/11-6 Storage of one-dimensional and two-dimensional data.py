# 存储和读取一维数据
def my_write():

    lst=['张三','李四','王五','陈六','麻七']
    with open('student.csv','w',encoding='utf-8') as file:
        file.writelines(','.join(lst))

def my_read():
    with open('student.csv','r',encoding='utf-8') as file:
        s = file.read()
        lst = s.split(',')
        print(lst)


#存储和读取二位数据
def my_write_table():
    lst = [
        ['商品名称','单价','采购数量'],
        ['水杯','98.5','20'],
        ['鼠标','89','100']
    ]
    with open('table.csv','w',encoding='utf-8') as file:
        for item in lst:
            line = ','.join(item)
            file.write(line)
            file.write('\n')


def my_read_table():
    data=[]   #存储读取的数据
    with open('table.csv','r',encoding='utf-8') as file:
        lst = file.readlines()  # 每一行是列表的一个元素
        for item in lst:
            new_list =item[:len(item)-1].split(',')
            data.append(new_list)
    print(data)



if __name__ == '__main__':
    #my_write()
    #my_read()
    #my_write_table()
    my_read_table()