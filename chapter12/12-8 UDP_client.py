from socket import socket, AF_INET, SOCK_DGRAM


#（1）创建一个套接字
send_socket = socket(AF_INET, SOCK_DGRAM)

#（2）准备发送数据
while True:

    #(2) 准备发送的数据
    data = input('客户说：>>>')

    #(3) 发送数据
    send_socket.sendto(data.encode('utf-8'), ('127.0.0.1', 8999))


    if data == 'bye':
        break

    #(4) 接收来自服务器的数据
    recv_data, addr = send_socket.recvfrom(1024)
    print('客服说：', recv_data.decode('utf-8'))


#（5）关闭套接字    
send_socket.close()