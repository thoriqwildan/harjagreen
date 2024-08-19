from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

# Create your views here.
@api_view(['POST', 'GET'])
def login_user(request):
    if request.method == 'GET':
        return Response({})
    
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"detail": "Not Found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=User)
        return Response({"token": token.key, "user": serializer.data})