def happy_birthday(name,age):
    # print(f'祝{name}生日快乐')
    # print('{0}岁 生日快乐'.format(age))
    print('祝'+name +'生日快乐')
    print('{0}岁 生日快乐'.format(age))

#TypeError: happy_birthday() missing 1 required positional argument: 'age'
#happy_birthday('温如水')


#TypeError: can only concatenate str (not "int") to str
#happy_birthday(7 ,'温如水')

happy_birthday('温如水',7)