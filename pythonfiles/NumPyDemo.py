import numpy as np

# 创建一个一维数组
a = np.array([1, 2, 3, 4, 5])
print("一维数组:")
print(a)

# 创建一个二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print("二维数组:")
print(b)

# 调整数组a的形状，使其与b的形状相匹配
reshaped_a = np.reshape(a, (a.shape[0], 1))
print("调整后的一维数组:")
print(reshaped_a)

# 数组运算，直接相加报错
# c = np.add(a, b)
# print("数组相加:")
# print(c)

# 数组函数
print("数组的和:", np.sum(a))
print("数组的最大值:", np.max(b))
print("数组的平均值:", np.mean(a))

# 数组的形状和大小
print("数组的形状:", a.shape)
print("数组的大小:", b.size)

# 数组的切片
print("数组切片:")
print(a[1:4])

# 数组的重塑
d = np.reshape(a, (5, 1))
print("重塑后的数组:")
print(d)
