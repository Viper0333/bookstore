from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirmation']  # removi bio e avatar
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                {"password_confirmation": "As senhas não coincidem."}
            )
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']  # removi bio e avatar
