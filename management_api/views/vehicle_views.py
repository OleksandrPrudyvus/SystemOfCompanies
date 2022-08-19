from rest_framework import generics, status
from rest_framework.response import Response
from management_api.models import Vehicle
from management_api.serializers import VehicleSerializer
from management_api.permissions import OnlyCompanyAdmin, IsCompanyWorker
from management_api.utils import CheckUserIsOfficeStaffMixin


class VehicleListCreateApiView(CheckUserIsOfficeStaffMixin, generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (OnlyCompanyAdmin,)

    def post(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        return self.create(request, *args, **kwargs)


class VehicleRetrieveUpdateDestroyApiView(CheckUserIsOfficeStaffMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (OnlyCompanyAdmin,)
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        return super().patch(request, *args, **kwargs)


class ProfileVehicleRetrieveApiView(generics.GenericAPIView):
    permission_classes = (IsCompanyWorker,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get(self, request):
        instance = Vehicle.objects.filter(pk=request.user.office_id)
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
