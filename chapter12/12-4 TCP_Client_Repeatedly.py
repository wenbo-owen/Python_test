import socket

#(1) 创建socket对象
client = socket.socket()

#(2) IP地址和主机端口，向服务器发送连接请求
print("正在连接服务器...")
ip = '127.0.0.1'
port = 8999   # 这里要写服务器的端口

client.connect((ip, port))

#(3) 发送数据
info = ''
while info != 'bye':

    send = input('请输入要发送的数据:')
    client.send(send.encode('utf-8'))

    if send == 'bye':
        break

    #(4) 接收数据
    info = client.recv(1024).decode('utf-8')
    print("接收到的数据为:", info)

#(5) 关闭socket
client.close()
print("客户端退出")