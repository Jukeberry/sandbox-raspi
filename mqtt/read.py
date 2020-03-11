import paho.mqtt.client as mqtt

mqttClient = mqtt.Client("jukeberry")
mqttClient.connect("192.168.0.12", 1883)


mqttClient.subscribe("stop/pushed")

def messageFunction(client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print (topic + message)

mqttClient.on_message = messageFunction
mqttClient.loop_start()