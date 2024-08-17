import random
import os
import os.path

#函数编程
def creat_filename():
    filename_lst=[]
    lst=['水果','烟酒','粮油','肉蛋','蔬菜',] #物资类别
    code=[str(item) for item in range(1,10)]+['A','B','C','D','E','F',]
    for i in range(1,21):
        file_name=''
        if i<10:
            file_name+='000'+str(i)
        elif i<100:
            file_name+='00'+str(i)
        file_name+='_'+random.choice(lst)
        #拼接识别码
        s=''
        for j in range(9):  #循环的作用是次数
            s+=random.choice(code)
        file_name +='_'+s
        filename_lst.append(file_name)
    return filename_lst

#创建文件的函数
def creat_file(filename):
    with open(filename,'w') as file:
        pass



if __name__ == '__main__':

    # 在指定的路径下创建文件
    path = './data'
    if not os.path.exists(path):
         os.mkdir(path)

    lst=creat_filename()  #获取文件名
    for item in lst:
        #creat_file('./data/'+item+'.txt')
        creat_file(os.path.join(path,item)+'.txt')

    # 开始创建




