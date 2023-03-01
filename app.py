# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 17:48
# @Author  : Li Xiaoyu

import os
import uuid
from tempfile import TemporaryDirectory
from celery_tasks.tasks.word_task import word_detect_info
from celery_tasks.celery_app import celery_app
from celery.result import AsyncResult

## flask
from flask import Flask, request, make_response, render_template, jsonify, url_for

app = Flask(__name__)


def warp_resp(res, status=400, headers={'Content-Type': 'application/json'}):
    resp = make_response(jsonify(res), status)
    resp.headers = headers
    return resp


# 调用服务
@app.route('/word_detect', methods=['POST'])
def word_detect():
    imf = request.files.get('inputfile')
    userinfo = request.form.get('userinfo')
    caseid = request.form.get('caseid')
    with TemporaryDirectory() as tmp_dir:
        outputs = os.path.join(tmp_dir, str(uuid.uuid4()))
        if not os.path.exists(outputs):
            os.makedirs(outputs)
        input_file = os.path.join(tmp_dir, imf.filename)
        imf.save(input_file)
        result = word_detect_info.delay(caseid, userinfo, input_file)
        summary = {"taskID": result.id,
                   "location": str(url_for('get_task_state', task_id=result.id))
                   }
        return warp_resp(summary, 202)


# 查询状态
@app.route('/tasks/<string:task_id>/state')
def get_task_state(task_id):
    result = AsyncResult(task_id, app=celery_app)
    summary = {
        "state": result.state,
        "result": result.result,
        "id": result.id,
    }
    return warp_resp(summary, 200)


if __name__ == '__main__':
    app.run('0.0.0.0', 9001, debug=False)
