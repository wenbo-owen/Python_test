def my_write(s):

    #打开(创建文件)文件
    file = open('b.txt', 'a', encoding='utf-8')
    #(2) 写入内容
    file.write(s)
    file.write('\n')
    #(3) 关闭
    file.close()


#向文件中写列表
def my_write_list(file,lst):
    f = open(file, 'a', encoding='utf-8')
    f.writelines(lst)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    #my_write('这个世界你好吗？')
    #lst = ['温博','王倩','米果']  #温博王倩米果
    lst1=['姓名\t','年龄\t','成绩\n','张三\t','30\t','98\n']
    #my_write_list('b.txt',lst)
    my_write_list('c.txt', lst1)