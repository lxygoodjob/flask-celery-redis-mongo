# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 17:48
# @Author  : Li Xiaoyu
from datetime import datetime

## celery
from celery_tasks.celery_app import celery_app

## redis
from redis_tasks.redis_util import redis_session

## mongodb
from pymongo import MongoClient
from mongo_tasks import mongo_util


# 调用celery
@celery_app.task()
def word_detect_info(caseid, userinfo, inputfile):
    """
    异步添加信息
    :param task_id:
            userinfo:
            wordfile:
    :return:
    """
    word_info = 'do something in wordfile'

    # PyMongo 不是进程安全，所以子进程需要创建自己的连接
    with MongoClient(mongo_util.URI) as client:
        db = client[mongo_util.WORD_DETECT_TASK.name]
        word_info_col = db[mongo_util.WORD_DETECT_TASK.word_info_collection]
        word_info_col.update_one({"caseid": caseid, "userinfo": userinfo, "word_info": word_info},
                                 {"$set": {
                                     "status": "success",
                                     "update_time": datetime.utcnow()}},
                                 upsert=True
                                 )
    return {'result': 'completed',
            'caseid': caseid
            }
