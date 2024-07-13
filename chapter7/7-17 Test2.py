try:
    a = int(input('请输入第1条边长: '))
    b = int(input('请输入第2条边长: '))
    c = int(input('请输入第3条边长: '))

    if a+b>c and a+c>b and c+b>a :
        print('三角形的边长为 %d %d %d'%(a,b,c))
    else:
        raise Exception(a,b,c,'不能构成三角形')


except Exception as e:
    print(e)