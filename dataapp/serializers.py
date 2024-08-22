from rest_framework import serializers
from .models import Tool, SoilMoisture, Temperature

class SoilMoistureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoilMoisture
        fields = ['url', 'id', 'tool', 'moisture_level', 'recorded_at']

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ['url', 'id', 'tool', 'temp', 'humidity', 'recorded_at']

class ToolSerializer(serializers.HyperlinkedModelSerializer):
    tokenmqtt = serializers.CharField(source='user.mqtttoken', read_only=True)
    temperatures = TemperatureSerializer(many=True, read_only=True)
    SoilMoistures = SoilMoistureSerializer(many=True, read_only=True)

    class Meta:
        model = Tool
        fields = ['url', 'id', 'tokenmqtt', 'temperatures', 'SoilMoistures', 'created_at']
