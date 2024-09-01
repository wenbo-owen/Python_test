from socket import socket,AF_INET, SOCK_STREAM 

# AF_INET 用于Interrnet之间的进程通讯
# SOCK_STREAM 表示的事用TCP协议编程

#（1）创建一个套接字
server_socket = socket(AF_INET, SOCK_STREAM)

#（2）绑定地址
ip = '127.0.0.1'    #等同于localhost
port = 8999         # 端口的范围
server_socket.bind((ip, port))

#（3）开始监听
# 服务器处在监听状态，时刻等待着客户端的连接
server_socket.listen(5)
print('服务器已启动，等待客户端连接...')

# (4) 等待客户端连接
client_socket, client_addr = server_socket.accept()
print('客户端已连接，地址:', client_addr)
while True:
    # （5）接收客户端数据
    recv_data = client_socket.recv(1024)
    print('客户端发送的数据：', recv_data.decode('utf-8'))

    # （6）发送数据给客户端
    send_data = input('>>>')
    client_socket.send(send_data.encode('utf-8'))

    # （7）关闭套接字
    client_socket.close()
    break
print('服务器已关闭')