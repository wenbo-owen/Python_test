# coding=utf-8
import wx
import threading
from socket import socket,AF_INET,SOCK_STREAM

class WbClient(wx.Frame):
    def __init__(self,client_name):
        
        #调用父类的初始化方法
        #None : 没有父级窗口
        # id : 表示当前窗口的一个编号
        # pos:  窗体的打开位置
        # size: 窗体的大小，单位是像素，400宽，450高
        
        wx.Frame.__init__(self, None,id=1001,title=client_name+"的客户端界面",pos=wx.DefaultPosition,size=(400,450))  
        
        # 窗体中放一个面板，创建面板对象
        pl = wx.Panel(self) 

        # 面板上有个盒子
        box = wx.BoxSizer(wx.VERTICAL) #垂直放向上自动排版

        #可伸缩的网格布局
        fgz1 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局

        conn_btn = wx.Button(pl,size=(200,40), label='连接')  
        dis_conn_btn = wx.Button(pl,size=(200,40), label='断开') 

        #把两个按钮放到可伸缩的网格布局中
        fgz1.Add(conn_btn, 1, wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn, 1, wx.TOP|wx.RIGHT)

        #把可伸缩的网格布局放到盒子中
        box.Add(fgz1, 1, wx.ALIGN_CENTER)
       
        #只读文本框，显示聊天内容
        self.show_text = wx.TextCtrl(pl, size=(400, 210), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTER)

        #聊天文本框，显示聊天内容
        self.chat_text = wx.TextCtrl(pl, size=(400, 120), style=wx.TE_MULTILINE)
        box.Add(self.chat_text, 1, wx.ALIGN_CENTER)

        #可伸缩的网格布局
        fgz2 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局

        reset_btn = wx.Button(pl,size=(200,40), label='重置')  
        send_btn = wx.Button(pl,size=(200,40), label='发送') 

        #把两个按钮放到可伸缩的网格布局中
        fgz2.Add(reset_btn, 1, wx.TOP|wx.LEFT)
        fgz2.Add(send_btn, 1, wx.TOP|wx.RIGHT)

        #把可伸缩的网格布局放到盒子中
        box.Add(fgz2, 1, wx.ALIGN_CENTER)

        #将盒子放入面板当中
        pl.SetSizer(box)

        #self.show_text.AppendText('欢迎来到聊天室！')

        '''------------------以上代码是客户端界面的绘制-----------------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        #实例属性的设置
        self.client_name = client_name
        self.isConnected = False
        self.client_socket = None #设置客户端的socket对象为空

        #给发送按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON,self.send_to_server,send_btn)

        #给断开按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON,self.disconnect_to_server,dis_conn_btn)

        #给重置按钮绑定一个事件
        self.Bind(wx.EVT_BUTTON,self.reset_text,reset_btn)

    def reset_text(self,event):

        self.chat_text.Clear() #文本框中的内容就没有了 

    def disconnect_to_server(self,event):

        if self.isConnected:

            self.isConnected = False
            #发送断开信息给服务器
            self.client_socket.send('bye'.encode('utf-8'))
            
            # self.client_socket.close()
            # self.client_socket = None





    def send_to_server(self,event):

        if self.isConnected:

            input_data = self.chat_text.GetValue()
            if input_data != '':
                self.client_socket.send(input_data.encode('utf-8'))
                #发送完之后，清空文本框
                self.chat_text.SetValue('')

    def connect_to_server(self,event):
        
        if not self.isConnected:

            self.isConnected = True
            #tcp编程步骤
            server_host_port=('127.0.0.1',8888)
            self.client_socket = socket(AF_INET,SOCK_STREAM)
            #发送连接请求
            self.client_socket.connect(server_host_port)
            # 只要连接成功,发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))

            # 启动一个线程，客户端线程要与服务器会话线程进行通信
            client_thread = threading.Thread(target=self.recv_data)
            # 设置为守护线程
            client_thread.daemon = True
            #启动
            client_thread.start()



    
    #接收来自服务器端发过来的聊天信息
    def recv_data(self):
        # 如果是连接
        while self.isConnected:
            # 接收来自服务器的数据
            data = self.client_socket.recv(1024).decode('utf-8')
            # 显示到只读文本框中
            self.show_text.AppendText('欢迎来到聊天室'+'\n')
            self.show_text.AppendText('-'*40+'\n'+data+'\n')







if __name__ == '__main__':
    
    app = wx.App()
    # 创建自己的客户端对象
    name = input('请输入客户端名字：')
    wb = WbClient(name)

    # wb = WbClient('Python_温博')
    wb.Show()
    # 循环刷新显示
    app.MainLoop()