from .models import Tool, SoilMoisture, Temperature
from .serializers import ToolSerializer, SoilMoistureSerializer, TemperatureSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

# Create your views here.
class ToolViewSet(viewsets.ModelViewSet):
    serializer_class = ToolSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tool.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SoilMoistureViewSet(viewsets.ModelViewSet):
    serializer_class = SoilMoistureSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        tool_id = self.request.query_params.get('tool_id', None)

        # Jika tool_id diberikan, filter suhu berdasarkan tool tersebut
        if tool_id is not None:
            return SoilMoisture.objects.filter(tool__id=tool_id, tool__user=user)
        
        # Jika tidak ada tool_id, kembalikan semua suhu dari semua tools milik user
        return SoilMoisture.objects.filter(tool__user=user)

    def perform_create(self, serializer):
        tool_id = self.request.query_params.get('tool_id')
        if not tool_id:
            raise serializers.ValidationError("tool_id is required")
        try:
            tool = Tool.objects.get(id=tool_id, user=self.request.user)  # Pastikan tool milik user yang sedang login
        except Tool.DoesNotExist:
            raise NotFound("Tool not found or doesn't belong to the user")
        serializer.save(tool=tool)

class TemperatureViewSet(viewsets.ModelViewSet):
    serializer_class = TemperatureSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        tool_id = self.request.query_params.get('tool_id', None)

        if tool_id is not None:
            return Temperature.objects.filter(tool__id=tool_id, tool__user=user)
        return Temperature.objects.filter(tool__user=user)
    
    def perform_create(self, serializer):
        tool_id = self.request.query_params.get('tool_id')
        if not tool_id:
            raise serializers.ValidationError("tool_id is required")
        try:
            tool = Tool.objects.get(id=tool_id, user=self.request.user)
        except Tool.DoesNotExist:
            raise NotFound("Tool not found or doesn't belong to the user")
        serializer.save(tool=tool)
    