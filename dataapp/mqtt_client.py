import paho.mqtt.client as mqtt
import json
from .models import Tool, Temperature, SoilMoisture
import threading
import time

class MQTTClient:
    def __init__(self, broker, port=1883, username=None, password=None):
        self.broker = broker
        self.port = port
        self.client = mqtt.Client()
        self.username = username
        self.password = password
        self.subscribed_topics = set()

        if self.username and self.password:
            self.client.username_pw_set(self.username, self.password)

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.subscribe_to_all_tools()

    def on_message(self, client, userdata, msg):
        print(f"Message received on {msg.topic}: {msg.payload.decode()}")
        payload = json.loads(msg.payload.decode())
        token = msg.topic.split('/')[0]
        try:
            tool = Tool.objects.get(mqtttoken=token)
            if 'temperature' in payload and 'humidity' in payload and 'moisture' in payload:
                Temperature.objects.create(
                    tool=tool,
                    humidity=payload['humidity'],
                    temp=payload['temperature']
                )
                SoilMoisture.objects.create(
                    tool=tool,
                    moisture_level=payload['moisture']
                )
            else:
                print("Data not completed")
        except Tool.DoesNotExist:
            print(f"Tool with token {token} does not exist")

    def subscribe_to_all_tools(self):
        tools = Tool.objects.all()
        for tool in tools:
            topic = f'{tool.mqtttoken}/data'
            if topic not in self.subscribed_topics:
                self.client.subscribe(topic=topic)
                self.subscribed_topics.add(topic)

    def periodic_check_for_new_tools(self):
        while True:
            self.subscribe_to_all_tools()
            time.sleep(30)
    
    def connect(self):
        self.client.connect(self.broker, self.port, 60)
        threading.Thread(target=self.periodic_check_for_new_tools, daemon=True).start()
        self.client.loop_start()

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()