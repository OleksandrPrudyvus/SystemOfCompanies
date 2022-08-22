from rest_framework import generics, status
from rest_framework.response import Response
from management_api.models import Vehicle
from management_api.serializers import VehicleSerializer
from management_api.permissions import OnlyCompanyAdmin, IsCompanyWorker
from management_api.utils import CheckUserIsOfficeStaffMixin


class VehicleListCreateApiView(CheckUserIsOfficeStaffMixin, generics.ListCreateAPIView):
    """ApiView for get(list) and create Vehicle, accepts a GET, POST method"""

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (OnlyCompanyAdmin,)
    filterset_fields = ['office', 'user']

    def post(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        return Vehicle.objects.filter(company_id=self.request.user.company_id)


class VehicleRetrieveUpdateDestroyApiView(CheckUserIsOfficeStaffMixin, generics.RetrieveUpdateDestroyAPIView):
    """ApiView for get and change vehicle, accepts a GET, PUT, PATCH method"""

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = (OnlyCompanyAdmin,)
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        return self.put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        if not self.check_office_staff(request, *args, **kwargs):
            return Response({'msg': f'User is not office worker'})
        return self.patch(request, *args, **kwargs)


class ProfileVehicleRetrieveApiView(generics.ListAPIView):
    """ApiView for get my vehicles, accepts a GET method"""

    permission_classes = (IsCompanyWorker,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.filter(user=self.request.user)
