import wx
import threading
import time
from socket import socket,AF_INET,SOCK_STREAM   

class WbServer(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=1002, title="温博的服务端界面", pos=wx.DefaultPosition, size=(400, 450))
        # 窗体放一个面板
        pl = wx.Panel(self)

        # 面板上有个盒子
        box = wx.BoxSizer(wx.VERTICAL)  # 垂直放向上自动排版

        # 可伸缩的网格布局
        fgz1 = wx.FlexGridSizer(wx.HSCROLL)  # 水平方向布局

        start_server_btn = wx.Button(pl, size=(133, 40), label='启动服务')  # 按钮
        record_btn       = wx.Button(pl, size=(133, 40), label='保存聊天记录')  # 按钮
        stop_server_btn     = wx.Button(pl, size=(133, 40), label='停止服务')  # 按钮

        fgz1.Add(start_server_btn, 1, wx.TOP)
        fgz1.Add(record_btn, 1, wx.TOP)
        fgz1.Add(stop_server_btn, 1, wx.TOP)

        #将可伸缩的网格布局放到盒子中
        box.Add(fgz1, 1, wx.ALIGN_CENTER)

        
        #只读文本框，显示聊天内容
        self.chat_text = wx.TextCtrl(pl,size=(400, 410) ,style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.chat_text, 1, wx.ALIGN_CENTER)
        
        pl.SetSizer(box)

        '''----------------以上代码是界面的绘制代码-----------------'''
        ''''服务器功能实现的必要属性'''
        self.isOn = False  #存储服务器的启动状态，默认为False，默认没有启动
        self.host_port=('',8888) #服务器地址和端口
        self.server_socket = socket(AF_INET, SOCK_STREAM)  #存储服务器的socket对象

        #绑定IP地址和端口
        self.server_socket.bind(self.host_port)

        # 监听 服务器处在监听状态，时刻等待着客户端的连接
        self.server_socket.listen(5)
        #创建一个字典，存储与客服端对话的会话线程
        self.sesstion_thread_dict = {}  #key-value {客户端的名称key:会话线程value}

        #当鼠标点击“启动服务”按钮时，触发事件   绑定事件
        self.Bind(wx.EVT_BUTTON, self.start_server, start_server_btn)

        # 绑定聊条记录按钮
        self.Bind(wx.EVT_BUTTON, self.save_record, record_btn)

        # 绑定停止服务按钮
        self.Bind(wx.EVT_BUTTON, self.stop_server, stop_server_btn)


    def stop_server(self,event):

        print('服务器已停止服务')
        self.isOn = False



    def save_record(self,event):

        recode_data = self.chat_text.GetValue()
        with open('record.log','w',encoding='utf-8') as file:
            file.write(recode_data)


    def start_server(self,event):

        if self.isOn == False:
            #启动服务器
            self.isOn = True
            # 创建主线程对象，函数式创建主线程
            main_thread = threading.Thread(target=self.do_work)
            # 设置守护线程，父线程执行结束(窗体界面) 子线程也自动关闭
            main_thread.daemon=True
            # 启动主线程
            main_thread.start()


    def do_work(self):

        #判断isOn的值
        while self.isOn:

            #接收客户端的连接请求 等待
            sesstion_socket,client_addr = self.server_socket.accept()
            #客户端发送连接请求之后,发送过来的第一条数据为客户端的名称额
            user_name = sesstion_socket.recv(1024).decode('utf-8')
            
            print(user_name,sesstion_socket,'123')
            #创建一个会话线程对象
            sesstion_thread = SesstionThread(sesstion_socket,user_name,self)
            #存储到字典之中
            self.sesstion_thread_dict[user_name] = sesstion_thread
            #启动会话线程
            sesstion_thread.start()

            #输出服务器提示信息
            self.show_info_and_send_client('服务器提示',f'欢迎{user_name}进入聊天室',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


        #当isOn的值为False
        self.server_socket.close()


    def show_info_and_send_client(self,data_source,data,date_time):
        #字符串操作
        send_data = f'{data_source}:{data}\n时间：{date_time}'
        #只读文本框
        self.chat_text.AppendText('-'*40+'\n'+send_data+'\n')
        #每一个客服端都发送一次
        for client in self.sesstion_thread_dict.values():
            #如果当前会话是开启状态
            if client.isOn:
                client.client_socket.send(send_data.encode('utf-8'))



#服务器端会话线程的类
class SesstionThread(threading.Thread):
    
    def __init__(self,client_socket,user_name,server):
        
        #调用父类的初始化方法
        threading.Thread.__init__(self)
        self.client_socket =  client_socket
        self.user_name  =  user_name
        self.server = server
        self.isOn = True
    def run(self):
        print(f'客户端{self.name}已经和服务器连接成功，服务器启动一个会话线程')
        while self.isOn:
            #从客户端接收数据 存储到data中
            data = self.client_socket.recv(1024).decode('utf-8')
            #如果客户端点击断开按钮,先给服务器发送一句话,自定义消息  自定义的结束词语
            if data == 'bye':
                self.isOn = False
                #发送一条服务器通知
                self.server.show_info_and_send_client('服务器通知',f'{self.user_name}离开了聊天室',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
            else:
                #其它聊天信息显示给所有客户端,包含服务器也显示
                #调用刚才编写的方法
                #服务器发送给客户端
                self.server.show_info_and_send_client(self.user_name,data,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
                
        self.client_socket.close()


if __name__ == '__main__':
    
    # 初始化App()
    app = wx.App()
    # 创建窗口
    wb = WbServer()
    wb.Show()
    # 循环刷新显示
    app.MainLoop()