import datetime

def input_date():
    date_in = input("请输入日期，例如20120817：")
    date = date_in[0:4]+'-'+date_in[4:6]+'-'+date_in[6:8]   #切片 切出年 月 日
    #类型转换
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return date


if __name__ == '__main__':
    date = input_date()
    #输入间隔的天数
    num_in = eval(input('输入要间隔的天数'))
    date = date+datetime.timedelta(days=num_in)
    print(date)