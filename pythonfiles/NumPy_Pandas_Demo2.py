import numpy as np
import pandas as pd

# 创建一个NumPy数组
arr = np.array([1, 2, 3, 4, 5])

# 使用NumPy函数计算数组的平均值
mean = np.mean(arr)
print("数组的平均值:", mean)

# 创建一个Pandas的Series对象
series = pd.Series(arr)

# 使用Pandas函数计算Series的平均值
mean = series.mean()
print("Series的平均值:", mean)