import numpy as np
import pandas as pd

# 创建一个NumPy数组
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 将NumPy数组转换为Pandas DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])

# 在DataFrame中进行筛选和操作
filtered_df = df[df['C'] > 5]
df['D'] = df['A'] + df['B']
average = df['C'].mean()

# 将DataFrame保存到CSV文件
df.to_csv('data.csv', index=False)

# 从CSV文件读取DataFrame
new_df = pd.read_csv('data.csv')

# 使用NumPy和Pandas进行数据分析和计算
column_sums = df.sum()
row_means = df.mean(axis=1)
column_std = np.std(df, axis=0)

# 打印结果
print("DataFrame:\n", df)
print("\nFiltered DataFrame:\n", filtered_df)
print("\nAverage of column C:", average)
print("\nColumn sums:\n", column_sums)
print("\nRow means:\n", row_means)
print("\nColumn standard deviations:\n", column_std)