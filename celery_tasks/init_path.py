# -*- coding: utf-8 -*-
# @Time    : 2023/2/27 17:51
# @Author  : Li Xiaoyu
import os
import sys


def init_path():
    FILE_PATH = os.path.abspath(os.path.dirname(__file__))
    PROJECT_PATH = os.path.join(FILE_PATH, '..')

    sys.path.extend([])
