def lower_upper(x):

    lst = []
    for item in x:
        if 'A'<= item <='Z':
            lst.append(chr(ord(item)+32))
        elif 'a'<= item <='z':
            lst.append(chr(ord(item) - 32))
        else:
            lst.append(item)

    return ''.join(lst)


def lower_upper1(x):

    lst = []
    for item in x:
        if item.isupper():
            lst.append(item.lower())
        elif item.islower():
            lst.append(item.upper())
        else:
            lst.append(item)

    return ''.join(lst)



s = input('请输入一个字符串：')
print(s)
new_s = lower_upper1(s)
print(new_s)

