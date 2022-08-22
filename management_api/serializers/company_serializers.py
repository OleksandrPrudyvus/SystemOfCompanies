from rest_framework import serializers
from management_api.models import Company


class CompanySerializer(serializers.ModelSerializer):
    """Serializer that is a representation of the Company model"""
    class Meta:
        model = Company
        fields = ('name', 'address')
