#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import request,jsonify
import json,uuid,datetime
from conf import log


"""
{
    "uid":"",
    "target":["123","456"], 
    "msg":{}
}
"""

def event_get(mongo,hardwareId,etype):
    pass



def event_post(mongo,data):
    message = mongo.db.message
    date = datetime.datetime.now()
    data = json.loads(data)
    log.logger.info(data)
    uid = data['uid']
    msg = data['msg']
    log.logger.info(msg)
    message.insert(data)
    data.pop('_id')
    return jsonify({'result': data, 'code': 200})


