import os.path
print('获取目录或文件的绝对路径:',os.path.abspath('./b.txt'))
print('判断目录或文件在磁盘上是否存在:',os.path.exists('b.txt')) # 相对路径
print('判断目录或文件在磁盘上是否存在:',os.path.exists('newb.txt'))
print('判断目录或文件在磁盘上是否存在:',os.path.exists('好好学习.txt'))
print('拼接路径:',os.path.join(r'D:\Python_prj\Python_test\chapter11\b.txt'))

print('分隔文件的名和文件的后缀名:',os.path.splitext('b.txt')) #元组类型
print('提取文件名:',os.path.basename(r'D:\Python_prj\Python_test\chapter11\b.txt')) #b.txt
print('提取路径:',os.path.dirname(r'D:\Python_prj\Python_test\chapter11\b.txt')) #b.txt

print('判断一个路径是否是有效路径:',os.path.isdir(r'D:\Python_prj\Python_test\chapter11')) #b.txt
print('判断一个路径是否是有效路径:',os.path.isdir(r'D:\Python_prj\Python_test\chapter114')) #b.txt
print('判断一个路径是否是有效文件:',os.path.isfile(r'D:\Python_prj\Python_test\chapter11\b.txt')) #b.txt
print('判断一个路径是否是有效文件:',os.path.isfile(r'D:\Python_prj\Python_test\chapter11\bbbbb.txt')) #b.txt


