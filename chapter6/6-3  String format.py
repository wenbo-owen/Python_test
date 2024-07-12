"""
格式化字符串
"""
#(1)使用占位符进行格式化
name = "马冬梅"
age = 18
score = 98.5
#print(name + age + score)  #TypeError: can only concatenate str (not "int") to str
print('姓名：%s，年龄：%d，分数：%f' %(name,age,score))