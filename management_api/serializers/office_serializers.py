from rest_framework import serializers
from management_api.models import Office


class BaseOfficeSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=None)
    url = serializers.URLField(source='get_absolute_url')

    def save(self, **kwargs):
        self.company = self.context.get('request').user.company
        kwargs['company'] = self.company
        super().save(**kwargs)

    class Meta:
        model = Office
        fields = ('name', 'address', 'country', 'city', 'region', 'url', 'company')