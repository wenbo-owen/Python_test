'''

with语句:又称上下文管理器,在处理文件时,无论是否产生异常,
都能保证with语句执行完毕后关闭已经打开的文件,这个过程是自动的,
无需手动操作。

'''

def write_fun():
    with open('aa.txt','w',encoding='utf-8') as file:
        file.write('你好，我的名字叫温博~')

def read_fun():
    with open('aa.txt','r',encoding='utf-8') as file:
        s1 = file.read()
        print(type(s1),s1)

def copy(src_file,target_file):
    with open(src_file,'r',encoding='utf-8') as file1:
        with open(target_file,'w',encoding='utf-8') as file2:
            file2.write(file1.read())   # 将读取的内容直接写进文件

if __name__ == '__main__':
    write_fun()
    read_fun()
    #文件复制
    copy('./aa.txt','./dd.txt')
