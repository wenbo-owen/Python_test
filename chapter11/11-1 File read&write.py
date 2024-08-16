def my_write():
    #(1)(创建)打开文件
    file = open('a.txt','w',encoding='utf-8')
    #(2) 操作文件
    file.write('伟大的中国梦')
    #(3) 关闭
    file.close()

def my_read():

    # (1)(创建)打开文件
    file = open('a.txt','r',encoding='utf-8')
    # (2) 操作文件
    s = file.read()
    print(type(s),s)
    # (3) 关闭
    file.close()

if __name__ == '__main__':
    my_write()
    my_read()

