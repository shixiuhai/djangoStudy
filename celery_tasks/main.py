from celery import Celery

# 1. 创建 celery 实列对象
celery_app=Celery('meiduo')
# 2. 加载配置文件
celery_app.config_from_object('celery_task.config')
# 3. 自动注册异步任务
celery_app.autodiscover_tasks('celery_tasks.sms')
# 启动 celery 