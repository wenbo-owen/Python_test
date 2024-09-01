from socket import socket, AF_INET, SOCK_DGRAM

#(1)创建socket对象
send_socket = socket(AF_INET, SOCK_DGRAM)

# (2)准备发送数据
send_data = input('请输入要发送的数据：>>>')

# (3)指定接收方的IP地址和端口
ip = '127.0.0.1'
port = 8999

# (4)发送数据
send_socket.sendto(send_data.encode('utf-8'), (ip, port))

# (5)接收来自接收方的回复数据
recv_data, addr = send_socket.recvfrom(1024)
print('来自接收方的回复数据：', recv_data.decode('utf-8'))
print('数据地址为：', addr)

# (6)关闭套接字
send_socket.close()