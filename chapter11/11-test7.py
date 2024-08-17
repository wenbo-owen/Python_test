import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import array

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("实时波形图")
        self.setGeometry(100, 100, 800, 600)
        self.data = array.array('d')

        # 创建一个中心Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 设置布局
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # 创建一个PlotWidget
        self.plot_widget = pg.PlotWidget()
        layout.addWidget(self.plot_widget)
        self.N = 200
        # 配置PlotWidget
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setRange(xRange=[0, 200], yRange=[-1.2, 1.2], padding=0)
        self.plot_widget.setLabels(left='y / V', bottom='x / point', title='y = sin(x)') # 设置坐标轴标签和标题

        # 初始化数据
        self.data = np.zeros(200)
        self.curve = self.plot_widget.plot(self.data, pen='y')
        self.idx = 0
        # 定时器
        self.timer = pg.QtCore.QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(10)


    def update_plot(self):
       # global idx  # 声明idx为全局变量
        tmp = np.sin(np.pi / 50 * self.idx)  # 计算当前索引对应的正弦值
        if len(self.data) < self.N:  # 如果数组未满，则直接添加新数据
            self.data.append(tmp)
        else:  # 如果数组已满，则移除最旧的数据点，并添加新数据点
            self.data[:-1] = self.data[1:]
            self.data[-1] = tmp
        self.curve.setData(self.data)  # 更新曲线数据
        self.idx += 1  # 索引自增


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())