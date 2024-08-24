from typing import Any
from django.core.management.base import BaseCommand
from dataapp.mqtt_client import MQTTClient

class Command(BaseCommand):
    help = 'Start MQTT client to listen to topics'

    def handle(self, *args: Any, **options: Any):
        mqtt_client = MQTTClient(broker='server.pgridiy.or.id', username='harja', password='Harjasmart1234')
        mqtt_client.connect()
        import time
        try:
            while True:time.sleep(1)
        except KeyboardInterrupt:
            mqtt_client.disconnect()
            self.stdout.write(self.style.SUCCESS('MQTT Client stopped'))