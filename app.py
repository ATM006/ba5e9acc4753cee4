#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from strategy import auth
from conf import log
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    log.logger.info("call : login()")
    if request.method == 'POST':
        log.logger.debug("login post method")
        data = json.loads(request.get_data().decode('utf-8'))
        username = data['username']
        password = data['password']
        res = auth.authority_user(username, password)

    return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
