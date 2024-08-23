from rest_framework import serializers
from .models import Tool, SoilMoisture, Temperature

class SoilMoistureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoilMoisture
        fields = ['url', 'id', 'tool', 'moisture_level', 'recorded_at']
        read_only_fields = ['id', 'tool', 'recorded_at']

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Temperature
        fields = ['url', 'id', 'tool', 'temp', 'humidity', 'recorded_at']
        read_only_fields = ['id', 'tool', 'recorded_at']

class ToolSerializer(serializers.HyperlinkedModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = Tool
        fields = ['url', 'id', 'user_name', 'name', 'mqtttoken', 'created_at']
        read_only_fields = ['id', 'user_name', 'mqtttoken', 'created_at']

    def get_user_name(self, obj):
        return obj.user.username
