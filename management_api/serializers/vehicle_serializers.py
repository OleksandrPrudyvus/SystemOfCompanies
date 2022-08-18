from rest_framework import serializers
from management_api.models import Vehicle, Office, User
from management_api.utils import GetUserCompanyMixin


class VehicleSerializer(GetUserCompanyMixin, serializers.ModelSerializer):
    company = serializers.HiddenField(default=None)
    #office = serializers.ChoiceField(required=False, choices=Office.objects.all())
    # user = serializers.MultipleChoiceField(required=False, choices=User.objects.all())

    class Meta:
        model = Vehicle
        fields = (
            'name',
            'licence_plate',
            'model',
            'year_of_manufacture',
            'company',
            'office',
            'user'
        )