import socket 


#（1）创建一个套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#（2）绑定地址
ip = '127.0.0.1'    #等同于localhost
port = 8999         # 端口的范围
server_socket.bind((ip, port))

#（3）监听
server_socket.listen(5)
print('服务器已启动，等待客户端连接...')

# (4) 等待客户端连接
client_socket, client_addr = server_socket.accept()
print('客户端已连接，地址:', client_addr)

info = client_socket.recv(1024).decode('utf-8')     # 初始化


while info != 'bye':                                # 条件判断  
    
    # （5）接收客户端数据
    if info != '':
        print('客户端发送的数据：', info)

    # （6）发送数据给客户端
    send_data = input('>>>')
    client_socket.send(send_data.encode('utf-8'))

    if send_data == 'bye':
        break
    info = client_socket.recv(1024).decode('utf-8')

# （7）关闭套接字

client_socket.close()
server_socket.close()

print('服务器已关闭')