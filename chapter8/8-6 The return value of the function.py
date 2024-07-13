def calc(a,b):
    print(a+b)

calc(10,30)
print(calc(1,3))

print('-'*40)

def calc2(a,b):
    s = a+b
    return s # 将s 返回给函数的调用出处理

print(calc2(5,9))

get_s2 = calc2(calc2(1,2),3)
print(get_s2)


#返回值可以是多少
def get_sum(num):
    s =0 #累加和
    odd_sum=0
    even_sum=0
    for i in range(1,num+1):
        if i%2 !=0:
            odd_sum += i
        else:
            even_sum += i
        s+=i
    return s,odd_sum,even_sum  # 3个值

result = get_sum(10)
print('result的类型是{0}'.format(type(result)))
print(result)

print('-'*50)

#解包赋值

a,b,c = get_sum(100)
print(a,'--->',b,'--->',c)

