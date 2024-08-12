# 定义学生类，录入5个学生信息存储到列表中
class Student(object):
    def __init__(self,name,age,gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score
    def info(self):
        print(f'{self.name}  {self.age}  {self.gender}  {self.score}')

stu_lst= []
for i in range(5):
    stu_str = input(f'请输入第{i+1}位学生信息及成绩：')
    lst = stu_str.split("#")
    name = lst[0]
    age = int(lst[1])
    gender = lst[2]
    score = int(lst[3])
    stu_lst.append(Student(name,age,gender,score))

for item in stu_lst:
    item.info()
    for i in item:
        print(i,end=' ')
    print()


print('-'*50)
print(stu_lst)


#   '温博'#18#'男'#100
#[<__main__.Student object at 0x000002047945FB50>, <__main__.Student object at 0x000002047945F950>, <__main__.Student object at 0x000002047945FF90>, <__main__.Student object at 0x000002047945EBD0>, <__main__.Student object at 0x00000204795C00D0>]