import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图表和子图
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# 在第一个子图上绘制正弦函数
ax1.plot(x, y1, 'r', label='Sin(x)')
ax1.set_ylabel('Amplitude')
ax1.legend()

# 在第二个子图上绘制余弦函数
ax2.plot(x, y2, 'b', label='Cos(x)')
ax2.set_xlabel('Time')
ax2.set_ylabel('Amplitude')
ax2.legend()

# 添加标题和标签
plt.suptitle('Sine and Cosine Functions')

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()
