from rest_framework import serializers
from management_api.models import Office
from management_api.utils import GetUserCompanyMixin


class BaseOfficeSerializer(GetUserCompanyMixin, serializers.ModelSerializer):
    """Serializer that is a representation of the Office model"""
    company = serializers.HiddenField(default=None)
    url = serializers.URLField(source='get_absolute_url', required=False)

    class Meta:
        model = Office
        fields = ('id', 'name', 'address', 'country', 'city', 'region', 'url', 'company')