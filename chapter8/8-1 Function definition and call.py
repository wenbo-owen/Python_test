# 3usages 是被调用执行了3次
def get_sum(num):  #num 定义在函数调用处，形式参数
    s=0
    for i in range(1,num+1):
        s+=i
    print(f'1到{num}的累加和为：{s}')

get_sum(10)         # 10是 实际参数值
get_sum(100)        # 使用实际参数参与函数功能的实现
get_sum(1000)

