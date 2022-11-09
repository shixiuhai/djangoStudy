@cleray_app.task(name='send_sms_code') # 使用装饰器注册任务
def send_sms_code(value1:int,value2:str)->None:
    # 考虑到独立运行减少依赖关系
    # 放一个异步任务
    pass
# 异步调用
# send_sms_code.delay(mobile,sms_code)