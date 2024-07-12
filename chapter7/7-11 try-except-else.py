'''
try:
    pass
except ZeroDivisionError :
    pass
except ValueError:
    pass
else:
    pass

'''


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print('结果：', result)

except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException:
    print('未知异常')
else:
    print('计算结果为:{0}'.format(result))



