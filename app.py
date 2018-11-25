#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_pymongo import PyMongo
from flask import request,jsonify
from strategy import auth
from mongo import user_utils,events_utils
from conf import log
import json

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/chat"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


#用户登录
@app.route('/login', methods=['GET','POST'])
def login():
    log.logger.info("call : login()")
    if request.method == 'POST':
        log.logger.debug("login post method")
        data = json.loads(request.get_data().decode('utf-8'))
        res = user_utils.user_get(mongo, data['uid'])

        return res
    else:
        return jsonify({'result': '','code':403})

#用户注册
@app.route('/signin',methods=['GET','POST'])
def signin():
    log.logger.info("call : signin()")
    if request.method == "POST":
        log.logger.debug("login post method")
        data = json.loads(request.get_data().decode('utf-8'))
        data['uid'] = random.randint(1,10000)
        res =  user_utils.user_post(mongo, data)
        return res
    else:
        return jsonify({'result': '','code':403})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
