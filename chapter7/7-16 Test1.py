try:
    socre = int(input("请输入分数: "))
    if socre <0 or socre > 100:
        raise Exception('分数不正确')  #表述信息
except Exception as e:  # 捕获异常
    print(e)

else:
    print('分 数为：',socre)