from rest_framework import serializers
from management_api.models import User


class WorkerUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)
    email = serializers.EmailField()
    repeat_password = serializers.CharField(max_length=128, write_only=True)
    is_worker = serializers.HiddenField(default=True)
    company_id = serializers.HiddenField(default=None)
    url = serializers.URLField(source='get_absolute_url', read_only=True)


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'repeat_password')
        read_only = ('email', )
        extra_kwargs = {
            'password': {'write_only': True},
            'repeat_password': {'write_only': True},
        }