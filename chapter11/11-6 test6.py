'''


'''


import pyqtgraph as pg
import numpy as np
import array
from random import uniform

app = pg.mkQApp()
# 创建一个空的double类型数组用于存储数据
data = array.array('d')
print(type(data), data)
N = 200

# 创建一个图形窗口
win = pg.GraphicsWindow()
win.setWindowTitle(u"pyqtgraph逐点画波形图")
win.resize(800, 600)

# 在图形窗口中添加一个绘图区域
p = win.addPlot()
p.showGrid(x=True, y=True)  # 显示网格
p.setRange(xRange=[0, N - 1], yRange=[-1.2, 1.2], padding=0) # 设置x和y轴的范围及内边距
p.setLabels(left='y / V', bottom='x / point', title='y = sin(x)') # 设置坐标轴标签和标题
# 创建一个曲线并添加到绘图区域，设置画笔颜色为黄色
curve = p.plot(pen='y')
idx = 0


# 定义绘图数据的函数
def plotData():
    global idx                              # 声明idx为全局变量
    tmp = np.sin(np.pi / 50 * idx)          # 计算当前索引对应的正弦值
    if len(data) < N:                       # 如果数组未满，则直接添加新数据
        data.append(tmp)
    else:                                   # 如果数组已满，则移除最旧的数据点，并添加新数据点
        data[:-1] = data[1:]
        data[-1] = tmp
    curve.setData(data)  # 更新曲线数据
    idx += 1  # 索引自增

def plotRandom():
    global idx                              # 声明idx为全局变量
    tmp = uniform(-1,1)        # 计算当前索引对应的正弦值
    if len(data) < N:                       # 如果数组未满，则直接添加新数据
        data.append(tmp)
    else:                                   # 如果数组已满，则移除最旧的数据点，并添加新数据点
        data[:-1] = data[1:]
        data[-1] = tmp
    curve.setData(data)  # 更新曲线数据
    idx += 1  # 索引自增


timer = pg.QtCore.QTimer()
#timer.timeout.connect(plotData)
timer.timeout.connect(plotRandom)
timer.start(10)

# 启动PyQt5应用程序的主循环
app.exec_()