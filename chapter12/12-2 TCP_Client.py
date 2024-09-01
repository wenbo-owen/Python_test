import socket 

#(1) 创建socket对象
client = socket.socket()

#(2) IP地址和主机端口，向服务器发送连接请求
print("正在连接服务器...")
ip = '127.0.0.1'
port = 8999   # 这里要写服务器的端口

client.connect((ip, port)) 

#(3) 发送数据
client.send('hello world ,my name is wenbo '.encode('utf-8'))
print("发送数据成功")

#(4) 接收数据
data = client.recv(1024)
print("接收到的数据为:", data.decode('utf-8'))

#(5) 关闭socket
client.close()
print("客户端退出")