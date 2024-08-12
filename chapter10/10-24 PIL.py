from PIL import Image

#加载图片
im = Image.open('flower.jpg')
#print(type(im),im)

#提取RGB图像的颜色通道，返回结果是图像的副本
#系列解包复制
r,g,b = im.split()
# print(r)
# print(g)
# print(b)

om = Image.merge(mode='RGB',bands=(r,b,g))
om.save('new_flower.jpg')