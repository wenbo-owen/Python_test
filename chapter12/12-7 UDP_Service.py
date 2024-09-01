from socket import socket, AF_INET, SOCK_DGRAM

#(1) 创建socket对象
recv_socket = socket(AF_INET, SOCK_DGRAM)

#(2) 绑定IP地址和端口
recv_socket.bind(('127.0.0.1', 8999))

#(3) 接收数据

while True:

    print("等待接收数据...")
    rec_data, addr = recv_socket.recvfrom(1024)
    print("客户说:", rec_data.decode('utf-8'))
    if rec_data.decode('utf-8') == 'bye':
        break
    # (4) 准备回复对方的数据
    send_data = input("客服回:")

    # (5) 发送数据
    recv_socket.sendto(send_data.encode('utf-8'), addr)

#(6) 关闭socket
recv_socket.close()
print("服务端退出")