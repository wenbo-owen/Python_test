import numpy as np
import matplotlib.pyplot as plt

# 参数设置
fs = 10000  # 采样频率，至少为信号最高频率的两倍（奈奎斯特采样定理）
T = 1 / fs  # 采样周期
duration = 1e-3  # 信号持续时间，例如1毫秒
t = np.arange(0, duration, T)  # 时间向量

# 假设的三角波频率
f = 1000  # 频率为1 kHz
omega = 2 * np.pi * f  # 角频率

# 生成三角波
# 注意：这里使用了一个简单的三角波生成方法，通过取模和条件语句  
# 更高效的方法可能涉及使用numpy的向量化操作，但这里为了清晰起见，使用循环
y = np.zeros_like(t)
for i in range(len(t)):
    if t[i] < 1 / (2 * f):
        y[i] = 2 * f * t[i]
    elif t[i] < 1 / f:
        y[i] = 1 - 2 * f * (t[i] - 1 / (2 * f))
    elif t[i] < 3 / (2 * f):
        y[i] = -2 * f * (t[i] - 1 / f)
    else:
        y[i] = -(1 - 2 * f * (t[i] - 3 / (2 * f)))

    # 标准化电压值到0到1之间（可选）
y = (y + 1) / 2

# 绘制图形
plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title('1 kHz Triangular Wave Voltage Signal')
plt.xlabel('Time (s)')
plt.ylabel('Voltage')
plt.grid(True)
plt.show()