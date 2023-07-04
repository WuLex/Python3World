# 导入数组模块
import array

# 创建一个整数类型的数组
my_array = array.array('i', [1, 2, 3, 4, 5])

# 访问数组元素
print(my_array[0])  # 输出：1
print(my_array[3])  # 输出：4

# 修改数组元素
my_array[2] = 10
print(my_array)  # 输出：array('i', [1, 2, 10, 4, 5])

# 获取数组长度
length = len(my_array)
print(length)  # 输出：5

# 添加元素到数组末尾
my_array.append(6)
print(my_array)  # 输出：array('i', [1, 2, 10, 4, 5, 6])

# 在指定位置插入元素
my_array.insert(1, 7)
print(my_array)  # 输出：array('i', [1, 7, 2, 10, 4, 5, 6])

# 删除指定索引的元素
del my_array[3]
print(my_array)  # 输出：array('i', [1, 7, 2, 4, 5, 6])

# 删除指定值的第一个元素
my_array.remove(5)
print(my_array)  # 输出：array('i', [1, 7, 2, 4, 6])

# 数组切片操作
sub_array = my_array[1:4]
print(sub_array)  # 输出：array('i', [7, 2, 4])

# 连接两个数组
new_array = my_array + array.array('i', [8, 9, 10])
print(new_array)  # 输出：array('i', [1, 7, 2, 4, 6, 8, 9, 10])

# 重复数组元素
repeated_array = my_array * 3
print(repeated_array)  # 输出：array('i', [1, 7, 2, 4, 6, 1, 7, 2, 4, 6, 1, 7, 2, 4, 6])

# 遍历数组元素
for element in my_array:
    print(element)
