#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
from mqtt import mqttclass

mqtt = mqttclass.MyMQTTClass()
ret = mqtt.run()

"""

from mongo import user_utils
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://orchid:123456@192.168.1.11:27017/chat"
mongo = PyMongo(app)


data = '{\
"uid": 666,\
"createddate": "2018-05-09 18:44:37",\
"hashpassword": "1234561",\
"lastLogin": "2018-05-09 18:44:37",\
"metadata": {},\
"friendlist":["123","456"],\
"status": true,\
"username": "atm"\
}'


@app.route('/')
def hello_world():
    user_utils.user_post(mongo, data)
    return 'Hello World!\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

