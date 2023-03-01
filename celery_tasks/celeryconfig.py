# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 16:45
# @Author  : Li Xiaoyu
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import timedelta

# celery配置

# 消息代理
broker_url = 'redis://127.0.0.1:6379/0'
# 存储任务执行结果
result_backend = 'redis://127.0.0.1:6379/1'
# 任务的序列化方式
# task_serializer = 'json'
# 任务执行结果的序列化方式
# result_serializer = 'json'
# 任务过期时间
result_expires = 60 * 60 * 24
# 接受内容类型
accept_content = ['json']
# 超时再分配时间
broker_transport_options = {'visibility_timeout': 3600}
# 每个worker执行了多少任务就会死掉，避免内存泄露
worker_max_tasks_per_child = 500
# 时区设置，用于定时任务
timezone = 'Asia/Shanghai'
enable_utc = False

# 任务导入，包括异步任务和定时任务
# # 制定任务模块
# imports = (
#     'celery_tasks.tasks.word_task',
# )
# # 计划任务
# CELERYBEAT_SCHEDULE = {
#     'test_reminders': {
#         # task就是需要执行计划任务的函数
#         'task': 'run_server.test',
#         # 配置计划任务的执行时间，这里是每60秒执行一次
#         'schedule': timedelta(seconds=60),
#         # 传入给计划任务函数的参数
#         'args': None
#     },
# }
