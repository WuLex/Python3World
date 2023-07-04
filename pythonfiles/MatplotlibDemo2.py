import matplotlib.pyplot as plt

# 创建数据
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 30, 10, 15, 20]

# 创建图表并绘制条形图
plt.bar(categories, values)

# 添加标题和标签
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")

# 显示图表
plt.show()
