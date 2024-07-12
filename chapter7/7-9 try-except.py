try:

    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2
    print('结果：',result)

except ZeroDivisionError:
    print('除数为0')