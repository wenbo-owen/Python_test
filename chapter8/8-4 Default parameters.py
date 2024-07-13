def happy_birthday(name='温博',age=18):
    # print(f'祝{name}生日快乐')
    # print('{0}岁 生日快乐'.format(age))
    print('祝'+name +'生日快乐')
    print('{0}岁 生日快乐'.format(age))


happy_birthday()
happy_birthday('王倩')  # 位置传参
happy_birthday(age=19)  # 位置传参

#happy_birthday(19)  #19会赋值给哪个变量呢 19被传给name 报错


def fun(a,b=20):  # a为位置参数 ,b为默认值参数
    pass

#SyntaxError: non-default argument follows default argument
# 当位置参数和关键字参数同时存在的时候，位置参数在后会被报错
# def fun2(a=20,b): #语法错误
#     pass

# 当位置参数和关键字参数同时存在的时候，位置参数在前，默认参数在后

