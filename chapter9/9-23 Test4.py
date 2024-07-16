class Car():
    def __init__(self, type, no):
        self.type = type
        self.no = no

    def start(self):
        print('我是车，我能启动')

    def stop(self):
        print('我是车，我可以停止')

#出租车
class Taxi(Car):
    def __init__(self, type, no, company):
        super().__init__(type, no)
        self.company = company

    #重写父类的启动和停止方法
    def start(self):
        print('乘客您好')
        print(f'我i是{self.company}出租车公司，我的车牌是：{self.no}，您要去哪里')

    def stop(self):
        print('目的地到了，请您扫码付款，欢迎下次再来')

