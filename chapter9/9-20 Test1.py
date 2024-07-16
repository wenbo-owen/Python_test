from math import pi

class Circle():
    def __init__(self,r):
        self.radius = r

    def get_area(self):
        return self.radius * self.radius *pi
    def get_perimeter(self):
        return self.radius * 2 * pi

r = int(input('请输入圆的半径: '))
circle = Circle(r)

print('圆的面积是：{0:.2f}'.format(circle.get_area()))
print('圆的周长是：{0:.2f}'.format(circle.get_perimeter()))