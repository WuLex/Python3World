import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np

# 创建图形
fig, ax = plt.subplots()

# 绘制红色的背景
red_background = patch.Rectangle((0, 0), width=9, height=6, facecolor='#FF0000')
ax.add_patch(red_background)

# 五角星函数
def draw_star(center, radius, angle, color):
    x, y = center
    points = []
    for i in range(5):
        angle_i = angle + i * 2 * np.pi / 5
        points.append((x + radius * np.cos(angle_i), y + radius * np.sin(angle_i)))
        angle_i = angle + (i + 0.5) * 2 * np.pi / 5
        points.append((x + radius / 2 * np.cos(angle_i), y + radius / 2 * np.sin(angle_i)))
    star = patch.Polygon(points, closed=True, fill=True, color=color)
    ax.add_patch(star)

# 绘制大星星
draw_star((1.5, 4.5), 1, np.pi / 2, '#FFD700')

# 绘制小星星
small_star_centers = [(3, 5.5), (4, 4.5), (4, 3), (3, 2)]
for center in small_star_centers:
    draw_star(center, 0.5, np.pi / 5, '#FFD700')

# 设置坐标轴
ax.set_xlim(0, 9)
ax.set_ylim(0, 6)
ax.set_aspect(1)
plt.axis('off')

# 显示图像
plt.show()
