#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import jsonify
import requests
from conf import log

url = 'http://47.95.254.34:5120/iot/spi/'

exp = '{\
"createdDate": "",\
"createdBy": "",\
"username": "",\
"hashedPassword": "",\
"lastLogin": "",\
"status": "",\
"ext":{},\
"metadata": {}\
}'

"""需要重构"""
def authority_user(name,password):
    log.logger.info("call : authority_user(name,password)")
    res = requests.get(url + "users/" + name).json()
    print(res)
    if res["result"]["username"] == name and res["result"]["hashedPassword"] == password:
        return jsonify({'result': res, 'code': 200})
    else:
        return jsonify({'result': exp, 'code': 404})
