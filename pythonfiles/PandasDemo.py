import pandas as pd
import matplotlib.pyplot as plt


# 读取CSV文件
data = pd.read_csv('datatest.csv')

# 显示数据前几行
print(data.head())

# 显示数据统计摘要
print(data.describe())

# 选择特定的列
selected_columns = ['col1', 'col2']
subset = data[selected_columns]

# 过滤数据
filtered_data = data[data['col1'] > 100]

# 添加新列
data['new_column'] = data['col1'] + data['col2']

# 数据排序
sorted_data = data.sort_values(by='col1', ascending=False)

# 数据分组和聚合
grouped_data = data.groupby('col1').mean()

# 数据绘图
data.plot(x='col1', y='col2', kind='scatter')
# 绘制散点图
plt.show()

# 保存数据到新文件
filtered_data.to_csv('filtered_data.csv', index=False)
