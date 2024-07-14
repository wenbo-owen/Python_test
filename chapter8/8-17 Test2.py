def get_digit_sum(str):

    lst=[]
    for char in str:
        if char.isdigit():
            lst.append(int(char))

    s = sum(lst)


    return lst,s

string = input("请输入一段字符串,其中要包含数字:  ")

lst,s = get_digit_sum(string)
print('获取的数字列表是：',lst)
print('累加和为：',s)