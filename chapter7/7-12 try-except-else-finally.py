try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2


except ZeroDivisionError:
    print('除数不能为0')
except ValueError:
    print('不能将字符串转换为数字')
except BaseException:
    print('未知异常')
else:
    print('计算结果为:{0}'.format(result))

finally:                    #无论程序是否异常都需要执行
    print('程序执行结束')