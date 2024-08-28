"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dataapp.mqtt_client import MQTTClient
import threading
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

app = application

def start_mqtt_client():
    mqtt_client = MQTTClient(broker="server.pgridiy.or.id", username="harja", password="Harjasmart1234")
    mqtt_client.connect()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        mqtt_client.disconnect()

threading.Thread(target=start_mqtt_client, daemon=True).start()