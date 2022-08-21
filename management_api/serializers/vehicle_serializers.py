from rest_framework import serializers
from management_api.models import Vehicle, Office, User
from management_api.utils import GetUserCompanyMixin, CurrentCompanyDefault


class VehicleSerializer(GetUserCompanyMixin, serializers.ModelSerializer):
    company = serializers.HiddenField(default=CurrentCompanyDefault())
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'name',
            'licence_plate',
            'model',
            'year_of_manufacture',
            'company',
            'office',
            'user'
        )