# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 16:42
# @Author  : Li Xiaoyu
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from celery import Celery
from celery_tasks import celeryconfig
from celery_tasks.tasks import word_task

# 定义celery对象
celery_app = Celery(__name__)

# 引入配置信息
celery_app.config_from_object(celeryconfig)

# 自动搜寻异步任务
celery_app.autodiscover_tasks([word_task])
