'''

一、功能概述
readline()：每次读取文件中的一行内容。
readlines()：一次性读取文件的所有行，并以列表的形式返回。
二、返回值类型
readline()返回一个字符串，表示文件中的一行内容。如果文件已到达末尾，返回空字符串
readlines()返回一个列表，其中每个元素都是文件中的一行内容，包括换行符。

'''



import time

def show_info():
    print("输入提示数字，执行响应的操作：0.退出 1.查看登录日志")

# 记录日子
def write_loginfo(username):
    with open("log.txt", "a",encoding='utf-8') as file:
        s = f'用户名:{username},登录时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}\n'
        file.write(s)

#读日志的操作
def read_loginfo():
    with open('log.txt', 'r', encoding='utf-8') as file:
        while True:
            lines = file.readline()
            if lines == '':
                break
            else:
                print(lines)



if __name__ == '__main__':

    user = input("请输入用户名：")
    password = input("请输入密码：")

    if user == 'admin' and password == 'admin':
        print('密码正确！')
        write_loginfo(user)
        show_info()             #输入提示数字，执行响应的操作：0.退出 1.查看登录日志

        while True:
            num = eval(input('请输入提示数字：'))
            if num == 0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_loginfo()
                show_info()
            else:
                print('您输入的数字有误')
                show_info()

    else:
        print('输入密码有错误！')

