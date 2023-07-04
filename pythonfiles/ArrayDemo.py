# 创建一个列表
my_list = [1, 2, 3, 'four', 5.0]

# 访问列表元素
print(my_list[0])  # 输出：1
print(my_list[3])  # 输出：'four'

# 修改列表元素
my_list[2] = 'three'
print(my_list)  # 输出：[1, 2, 'three', 'four', 5.0]

# 添加元素到列表末尾
my_list.append(6)
print(my_list)  # 输出：[1, 2, 'three', 'four', 5.0, 6]

# 在指定位置插入元素
my_list.insert(1, 'inserted')
print(my_list)  # 输出：[1, 'inserted', 2, 'three', 'four', 5.0, 6]

# 删除指定索引的元素
del my_list[3]
print(my_list)  # 输出：[1, 'inserted', 2, 'four', 5.0, 6]

# 删除指定值的第一个元素
my_list.remove('four')
print(my_list)  # 输出：[1, 'inserted', 2, 5.0, 6]

# 获取列表长度
length = len(my_list)
print(length)  # 输出：5

# 遍历列表元素
for element in my_list:
    print(element)
