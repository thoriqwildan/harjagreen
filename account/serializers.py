from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise serializers.ValidationError("User not found.")
            
            if not user.check_password(password):
                raise serializers.ValidationError("Incorrect Password")
            
            data['user'] = user
        else:
            raise serializers.ValidationError('Must include username and password')
        return data

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'bio', 'profile_pic']
    
    def update(self, instance, validated_data):
        if 'profile_pic' in validated_data:
            instance.profile_picture.delete(save=False)  # Delete the old image if a new one is uploaded
        return super().update(instance, validated_data)
    
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'bio']

    def create(self, validated_data):
        username = validated_data.get('username')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        email = validated_data.get('email')
        password = validated_data.get('password')
        bio = validated_data.get('bio', '')

        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)  # Hashing the password
        user.save()

        # Create Profile for the user
        Profile.objects.create(user=user, bio=bio)

        return user
