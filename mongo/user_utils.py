#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import jsonify
import json, datetime
from conf import log

"""
{
    "_id":"",        #系统生成
    "uid":"",        #用户ID
    "createddate": "2018-05-09 18:44:37",    #创建日期
    "hashpassword": "1234561",        #密码hash，暂时名文
    "lastLogin": "2018-05-09 18:44:37",        #最后登陆时间
    "metadata": {},        #详细数据
    "friendlist":["123","456"]
    "status": true,        #登陆状态
    "username": "atm"        #用户名
}
"""


def user_get(mongo,uid):
	users = mongo.db.users
	res = users.find_one({"uid": uid})
	if res == None:
		return jsonify({'result': '','code':404})
	else:
		res.pop("_id")
		log.logger.info(res)
		return jsonify({'result':res,'code':200})


def user_get_all(mongo):
	users = mongo.db.users
	u = users.find()
	out = []
	for item in u:
		item.pop("_id")
		log.logger.info(item)
		out.append(item)
	return jsonify({'result':out,'code':200})



def user_post(mongo,data):
	"""创建用户信息"""
	users = mongo.db.users
	date = datetime.datetime.now()
	data = json.loads(data)
	log.logger.info(data)
	uid = data["uid"]
	if users.find_one({"uid":uid}) == None:
		data['createddate'] = date.strftime("%Y-%m-%d %H:%M:%S")
		data['lastLogin'] = date.strftime("%Y-%m-%d %H:%M:%S")
		data['status'] = True
		log.logger.info(data)
		users.insert(data)
		data.pop('_id')
		data = json.dumps(data)
		return jsonify({'result':data,'code':200})
	else:
		return jsonify({'result': '','code':403})


def user_put(mongo,data):
	"""更新用户信息"""
	log.logger.info("call : user_post(mongo,data)")
	users = mongo.db.users
	data = json.loads(data)
	date = datetime.datetime.now()
	uid = data["uid"]
	res = users.find_one({"uid": uid})
	if res != None:
		users.remove({"uid": uid})
		res = data
		log.logger.info(res)
		users.insert(res)
		res.pop("_id")
		return jsonify({'result':res,'code':200})
	else:
		return jsonify({'result': '','code':403})


def user_del(mongo,uid):
	users = mongo.db.users
	res = users.find_one({"uid": uid})
	if res == None:
		return jsonify({'result': '','code':404})
	else:
		users.remove({"uid": uid})
		res.pop("_id")
		log.logger.info(res)
		return jsonify({'result':res,'code':200})
