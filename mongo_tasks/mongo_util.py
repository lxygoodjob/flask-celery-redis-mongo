# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 17:07
# @Author  : Li Xiaoyu

HOST = '127.0.0.1'
PORT = 27017

USER = None
PASSWD = None

if USER is None or PASSWD is None:
    URI = "mongodb://{HOST}:{PORT}/".format(HOST=HOST, PORT=PORT)
else:
    URI = "mongodb://{USER}:{PASSWD}@{HOST}:{PORT}/".format(USER=USER, PASSWD=PASSWD, HOST=HOST, PORT=PORT)


class WORD_DETECT_TASK(object):
    name = 'word_detect_task'
    word_info_collection = 'word_info'
