import os

print('当前的工作路径',os.getcwd())
print('-'*40)
lst = os.listdir()
print('当前路径下的所有目录及文件')
print(lst)
# for i in lst:
#     print(i,end='\n')
print('-'*40)
print('指定路径下的所有目录及文件')
print(os.listdir('D:\Python_prj\Python_test'))

print('-'*40)
#创建目录
#os.mkdir('好好学习')  # 文件存在 报错
#os.makedirs('./aa/bb/cc')
#删除目录
#os.rmdir('./好好学习')  #如果删除目录不存在会保存
#os.removedirs('./aa/bb/cc')

#改变当前的工作路径
os.chdir('D:\Python_prj')
print('当前的工作路径')
print(os.getcwd())  #再写代码，工作路径就是D:/pythonpro

# 遍历目录树
for dirs,dirlst,filelst in os.walk('d:/python_prj'):
    print(dirs)
    print(dirlst)
    print(filelst)
