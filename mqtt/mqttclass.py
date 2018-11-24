#!/usr/bin/python3
# -*- coding: utf-8 -*-


import paho.mqtt.client as mqtt
import json
from conf import log


class MyMQTTClass(mqtt.Client):



    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: " + str(rc))

    def on_message(self, mqttc, obj, msg):
        log.logger.info("call : on_message(self, mqttc, obj, msg)")
        data = json.loads(msg.payload.decode("utf-8"))
        log.logger.info(data)
        target = data['details']['target']
        for item in target:
            print item
            self.publish("/test/output/" + item, '{"test":"123"}')

    def on_publish(self, mqttc, obj, mid):
        print("mid: " + str(mid))


    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: " + str(mid) + " " + str(granted_qos))

    #log.logger.info

    def on_log(self, mqttc, obj, level, string):
        print(string)

    #log.logger.info

    def run(self):
        self.connect("47.95.254.34", 1883, 60)
        log.logger.info("mqtt run ...")
        self.subscribe("/test/input/json", 0)
        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc


