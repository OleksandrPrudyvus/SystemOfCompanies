from django.contrib.auth import authenticate
from rest_framework import serializers
from management_api.models import User
from management_api.utils import CurrentUsernameDefault


class BaseUserSerializer(serializers.ModelSerializer):
    """Base Serializer that is a representation of the User model"""
    repeat_password = serializers.CharField(max_length=128, write_only=True)
    username = serializers.HiddenField(default=CurrentUsernameDefault())

    def create(self, validated_data, *args, **kwargs):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance: User, validated_data: dict):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        password = validated_data.get('password', instance.password)
        instance.password = password
        instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'username', 'email', 'password', 'repeat_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class AuthUserSerializer(serializers.Serializer):
    """Serializer that is a representation of the user model and is used for authorization"""
    email = serializers.CharField(label=("email"), write_only=True)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(label=("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                username=email, password=password)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
