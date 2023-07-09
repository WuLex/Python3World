from celery import Celery

# 创建一个Celery实例
app = Celery('tasks', broker='redis://localhost:6379/0')

# 定义任务
@app.task
def add(x, y):
    return x + y