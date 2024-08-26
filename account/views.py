from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, ProfileSerializer, LoginSerializer, RegisterSerializer
from django.contrib.auth.models import User
from .models import Profile

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class LoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication] #auth classnya bro
    permission_classes = [IsAuthenticated] #permission
    http_method_names = ['post', 'put', 'patch']

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    http_method_names = ['post']  # Only allow POST method

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        return Response({
            "user": {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
            },
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)
    



#class RegisterUser(APIView):
#     """
#     Ini format sign up nya
#         {
#             "user": {
#                 \t"username": "johndoe",
#                 \t"email": "johndoe@example.com",
#                 \t"password": "johndoooe"
#                 \t"first_name": "John",
#                 \t"last_name": "Doe"
#             },
#             "bio": "Software Developer",
#         }
#         """

#     def get(self, request):
#         return Response({})
    
#     def post(self, request):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             user = User.objects.get(username=serializer.data['user']['username'])
#             print(serializer.data['user']['username'])
#             print(user)
#             user.set_password(serializer.data['user']['password'])
#             user.save()
#             token, created = Token.objects.get_or_create(user=user)

#             try:
#                 profile = Profile.objects.get(user=user)
#             except Profile.DoesNotExist:
#                 return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND) 
#             serializer = ProfileSerializer(profile)

#             return Response({"token": token.key, "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class LoginUser(APIView):
#     def get(self, request):
#         return Response({})
    
#     def post(self, request):
#         try:
#             user = get_object_or_404(User, username=request.data['username'])
#             print(user.check_password(request.data['password']))
#             if not user.check_password(request.data['password']):
#                 return Response({"detail": "Not Found."}, status=status.HTTP_404_NOT_FOUND)
#             token, created = Token.objects.get_or_create(user=user)
#             serializer = UserSerializer(instance=user)
#             return Response({"token": token.key, "user": serializer.data})
#         except:
#             user

# class ProfileUser(APIView):
#     authentication_classes = [SessionAuthentication, TokenAuthentication] #auth classnya bro
#     permission_classes = [IsAuthenticated] #permission

#     def get(self, request):
#         user = request.user
#         try:
#             profile = Profile.objects.get(user=user)
#         except Profile.DoesNotExist:
#             return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)