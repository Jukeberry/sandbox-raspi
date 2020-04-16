#!/usr/bin/env python
##import pygame
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import paho.mqtt.client as mqtt
import datetime
import json
import time

def song(i):
    switcher={
        96675065265: "music/ParanoidAndroid.mp3",
        664003290249: "music/Creep.mp3",
        649586696873: "music/HighAndDry.mp3",
        711986787821: "music/BonfireHeart.mp3"
    }
    return switcher.get(i,"INVALID");

mqttTransport = "websockets"
mqttHost = "mr1nljqp0y1g2d.messaging.solace.cloud"
mqttPort = 21128
mqttUser = "solace-cloud-client"
mqttPassword = "7ide7v7illr1fs4bsio3ls26f0"

reader = SimpleMFRC522()
mqttClient = mqtt.Client("jukeberry", transport=mqttTransport)
mqttClient.username_pw_set(username=mqttUser,password=mqttPassword)
mqttClient.connect(mqttHost, mqttPort)
try:

    while(True):
        id, text = reader.read()
        now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S%zZ")
        print("id:" + str(id))
        print("text:" + str(text))

        message = {"id": str(id), "text": text, "sentAt": now }
        print (message)
        mqttClient.publish("card/presented", json.dumps(message))
        
        time.sleep(1);
except KeyboardInterrupt:         
    GPIO.cleanup()
    raise
finally:
    GPIO.cleanup()
