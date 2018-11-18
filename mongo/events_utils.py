#!/usr/bin/python3
# -*- coding: utf-8 -*-


from flask import request,jsonify
import json,uuid,datetime

exp = '{\
"eventType":"",\
"siteToken":"",\
"eventDate":"",\
"receivedDate":"",\
"hardwareId":"",\
"metadata":{},\
"ext":{},\
"eventbody":[]\
}'


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






def event_post(mongo,data,devId,etype):
	devices = mongo.db.devices
	date = datetime.datetime.now()
	ex = json.loads(exp)
	hardwareId = data["hardwareId"]
	if hardwareId != devId or data["eventType"] != etype:
		return jsonify({'result': ex, 'code': 403})

	if etype == 'DevicesData':
		edata = mongo.db.eventsdata
		if devices.find_one({"hardwareId": hardwareId}) == None:
			return jsonify({'result': ex, 'code': 403})
		else:
			ex["eventType"] = data["eventType"]
			ex["siteToken"] = data["siteToken"]
			ex["eventDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
			ex["receivedDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
			ex["hardwareId"] = hardwareId
			ex["metadata"] = data["metadata"]
			ex["eventbody"] = data["eventbody"]
			ex["ext"] = data["ext"]

			print(ex)
			edata.insert(ex)
			ex.pop("_id")
			return jsonify({'result': ex, 'code': 200})


	elif etype == 'UserCommands':
		ecommands = mongo.db.commands
		if devices.find_one({"hardwareId": hardwareId}) == None:
			return jsonify({'result': ex, 'code': 403})
		else:
			ex["eventType"] = data["eventType"]
			ex["siteToken"] = data["siteToken"]
			ex["eventDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
			ex["receivedDate"] = date.strftime("%Y-%m-%d %H:%M:%S")
			ex["hardwareId"] = hardwareId
			ex["metadata"] = data["metadata"]
			ex["eventbody"] = data["eventbody"]
			ex["ext"] = data["ext"]

			print(ex)
			ecommands.insert(ex)
			ex.pop("_id")
			return jsonify({'result': ex, 'code': 200})
	else:
		return jsonify({'result': ex, 'code': 403})