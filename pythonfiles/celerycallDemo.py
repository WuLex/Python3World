from tasks import add

result = add.delay(4, 6)  # 异步调用任务
print("任务已提交，结果将在稍后返回。")

# 等待任务完成并获取结果
print("任务结果：", result.get())