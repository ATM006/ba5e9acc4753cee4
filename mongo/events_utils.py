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
	devices = mongo.db.devices
	ex = json.loads(exp)
	res = devices.find()
	if etype == 'DevicesData':
		edata = mongo.db.eventsdata
		if res == None:
			return jsonify({'result': ex, 'code': 404})
		else:
			e = edata.find({"hardwareId": hardwareId,"eventType":"DevicesData"})
			out = []
			for item in e:
				item.pop("_id")
				print(item)
				out.append(item)

			return jsonify({'result': out, 'code': 200})

	elif etype == 'UserCommands':
		ecommands = mongo.db.commands
		if res == None:
			return jsonify({'result': ex, 'code': 404})
		else:
			e = ecommands.find({"hardwareId": hardwareId,"eventType":"UserCommands"})
			out = []
			for item in e:
				item.pop("_id")
				print(item)
				out.append(item)

			return jsonify({'result': out, 'code': 200})

	else:
		return jsonify({'result': ex, 'code': 403})






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


