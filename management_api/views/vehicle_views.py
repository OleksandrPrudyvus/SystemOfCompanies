from rest_framework import generics
from management_api.models import Vehicle
from management_api.serializers import VehicleSerializer
from management_api.permissions import OnlyCompanyAdmin


class VehicleListCreateApiView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (OnlyCompanyAdmin,)

    def post(self, request, *args, **kwargs):
        if request.data['office']:
            print(request.data)
        return self.create(request, *args, **kwargs)


