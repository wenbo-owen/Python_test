from socket import socket, AF_INET, SOCK_DGRAM

#(1) 创建socket对象
recv_socket = socket(AF_INET, SOCK_DGRAM)

#(2) 绑定IP地址和端口
recv_socket.bind(('127.0.0.1', 8999))

#(3) 接收数据   
print("等待接收数据...")
data, addr = recv_socket.recvfrom(1024)
print("接收到的数据为:", data.decode('utf-8'))

#(4) 准备回复对方的数据

data = input("请输入要回复的数据:")
recv_socket.sendto(data.encode('utf-8'), addr)


#(5) 关闭socket
recv_socket.close()
print("客户端退出")