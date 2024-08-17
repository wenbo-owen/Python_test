'''

json.dumps(obj)    将Python数据类型转成JSON格式过程，编码过程
json.loads(s)        将JSON格式字符串转成Python数据类型，解码过程
json.dump(obj,file)    与dumps()功能相同，将转换结果存储到文件file中
json.load(file)    与loads()功能相同，从文件file中读入数据

'''

import json

#准备高维数据, 是列表

lst =[

    {'name':'温博','age':18,'score':90},
    {'name':'王倩','age':18,'score':92},
    {'name':'米果','age':5,'score':95},

]

#ensure_asc 正常显示中文,indent增加数据的缩进,美观用的
# 编码过程
s = json.dumps(lst,ensure_ascii=False,indent=4)
print(type(s))  # str
print(s)

# 解码
lst2 = json.loads(s)    #<class 'list'>
print(type(lst2))
print(lst2)

# 编码到文件中
with open('student.txt','w') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)  #格式好看

#解码到程序
with open('student.txt','r') as file:
    s1 = json.load(file)            # 直接是列表类型了
    print(f'type(s1)={type(s1)}\n',s1)