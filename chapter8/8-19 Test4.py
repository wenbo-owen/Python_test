def get_find(s,lst):
    for item in lst:
        if s == item:
            return True
    else:
        return False

lst = ['hello','world','python']
s = input("输入需要查找的字符串：")
result = get_find(s,lst)


#三目运算符
print('存在' if result else '不存在')