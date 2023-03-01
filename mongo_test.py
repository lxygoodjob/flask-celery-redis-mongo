# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 15:14
# @Author  : Li Xiaoyu

from datetime import datetime
from pymongo import MongoClient
from mongo_tasks import mongo_util

with MongoClient(mongo_util.URI) as client:
    db = client[mongo_util.WORD_DETECT_TASK.name]
    word_info_col = db[mongo_util.WORD_DETECT_TASK.word_info_collection]
    print(word_info_col)
    word_info_col.update_one({"caseid": '123', "userinfo": 'lxy', "word_info": 'word_info_test'},
                             {"$set": {
                                 "status": "success",
                                 "update_time": datetime.utcnow()}},
                             upsert=True)
    print(word_info_col)