import prettytable as pt

def show_ticket(row_name):
    tb = pt.PrettyTable()  #创建一个表格
    tb.field_names = ["行号", "座位1", "座位2","座位3","座位4","座位5","座位6"]
    for item in range(1,row_name+1):
        lst = [f'第{item}行','有票','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)


def choose_ticket(row_name,row,colum):
    tb = pt.PrettyTable()
    tb.field_names = ["行号", "座位1", "座位2","座位3","座位4","座位5","座位6"]
    for i in range(1,row_name+1):
        lst = [f'第{i}行', '有票', '有票', '有票', '有票', '有票', '有票']
        if (int(row)==i):
            lst[int(colum)] = '已售'
        tb.add_row(lst)
    print(tb)






if __name__ == '__main__':
    show_ticket(6)
    choose_name = input('请输入要买的座位号,例如(4,3)')
    row,colum = choose_name.split(',')
    choose_ticket(6,row,colum)