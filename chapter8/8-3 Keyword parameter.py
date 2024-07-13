def happy_birthday(name,age):
    # print(f'祝{name}生日快乐')
    # print('{0}岁 生日快乐'.format(age))
    print('祝'+name +'生日快乐')
    print('{0}岁 生日快乐'.format(age))

#关键字传参
happy_birthday(age=17,name='温博')  # 必须与函数定义参数名相同
#TypeError: happy_birthday() got an unexpected keyword argument 'name1'
#happy_birthday(age=17,name1='温大博')

happy_birthday('温博',age=17)  #OK
happy_birthday(name='温博',17)  # SyntaxError: positional argument follows keyword argument


# 位置参数在前 关键字参数在后