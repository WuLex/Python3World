from tasks import resize_image, convert_image

# 异步调用图像缩放任务
resize_result = resize_image.delay('input.jpg', 'resized.jpg', 800, 600)
print("图像缩放任务已提交，结果将在稍后返回。")

# 异步调用图像格式转换任务
convert_result = convert_image.delay('input.jpg', 'converted.png', 'PNG')
print("图像格式转换任务已提交，结果将在稍后返回。")

# 等待任务完成并获取结果
resized_image_path = resize_result.get()
converted_image_path = convert_result.get()

print("图像缩放任务结果：", resized_image_path)
print("图像格式转换任务结果：", converted_image_path)