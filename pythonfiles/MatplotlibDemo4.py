import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)

# 创建图表和子图
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))

# 在第一个子图上绘制正弦函数
ax1.plot(x, y1, 'r', label='Sin(x)')
ax1.set_title('Sine Function')
ax1.set_xlabel('X-axis')
ax1.set_ylabel('Y-axis')
ax1.legend()

# 在第二个子图上绘制余弦函数
ax2.plot(x, y2, 'g', label='Cos(x)')
ax2.set_title('Cosine Function')
ax2.set_xlabel('X-axis')
ax2.set_ylabel('Y-axis')
ax2.legend()

# 在第三个子图上绘制正切函数
ax3.plot(x, y3, 'b', label='Tan(x)')
ax3.set_title('Tangent Function')
ax3.set_xlabel('X-axis')
ax3.set_ylabel('Y-axis')
ax3.legend()

# 在第四个子图上绘制正弦和余弦函数
ax4.plot(x, y1, 'r', label='Sin(x)')
ax4.plot(x, y2, 'g', label='Cos(x)')
ax4.set_title('Sine and Cosine Functions')
ax4.set_xlabel('X-axis')
ax4.set_ylabel('Y-axis')
ax4.legend()

# 调整布局
plt.tight_layout()

# 显示图表
plt.show()
