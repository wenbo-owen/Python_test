def copy(src,new_path):
    # 文件的复制就是边读边写操作
    #(1) 打开源文件
    file1 = open(src,'rb')
    #(2) 打开目标文件
    file2 = open(new_path,'wb')

    #(3)开始复制，边读边写
    s = file1.read()  # 源文件读取所有
    file2.write(s)  #向目标文件写入所有

    #(4) 关闭
    file2.close()
    file1.close()  #先打开的后关，后打开的先关

if __name__ == '__main__':
    copy('../chapter10/flower.jpg','./copy_flower.jpg')
    print('文件复制完毕')