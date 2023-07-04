def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # 已经排序的元素不需要再比较
        for j in range(0, n-i-1):
            # 如果当前元素大于下一个元素，则交换它们
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 示例用法
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("排序后的数组:")
for i in range(len(arr)):
    print(arr[i])
