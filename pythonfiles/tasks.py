import os
from celery import Celery
from PIL import Image

# 创建一个Celery实例
app = Celery('tasks', broker='redis://localhost:6379/0')

# 定义任务：图像缩放
@app.task
def resize_image(image_path, output_path, width, height):
    # 打开图像
    image = Image.open(image_path)

    # 调整大小
    resized_image = image.resize((width, height))

    # 保存图像
    resized_image.save(output_path)

    return output_path

# 定义任务：图像格式转换
@app.task
def convert_image(image_path, output_path, format):
    # 打开图像
    image = Image.open(image_path)

    # 转换格式
    image.convert(format).save(output_path)

    return output_path