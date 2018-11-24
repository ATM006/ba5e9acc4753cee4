#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
from mqtt import mqttclass

mqtt = mqttclass.MyMQTTClass()
ret = mqtt.run()

"""

from mongo import user_utils,events_utils
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://127.0.0.1:27017/chat"
mongo = PyMongo(app)


data = '{\
"uid": 662,\
"createddate": "2018-05-09 18:44:37",\
"hashpassword": "1234561",\
"lastLogin": "2018-05-09 18:44:37",\
"metadata": {},\
"friendlist":["123","456"],\
"status": true,\
"username": "atmii"\
}'

msg = '{\
"uid":123,\
"target":["123","456"], \
"time":"2018-05-09 18:44:37",\
"msg":"hello word!"\
}'



@app.route('/')
def hello_world():
    #ret = user_utils.user_post(mongo, data)
	#ret = user_utils.user_put(mongo, data)
	#ret = user_utils.user_get(mongo, 663)
	ret = events_utils.event_post(mongo,msg)
	return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

