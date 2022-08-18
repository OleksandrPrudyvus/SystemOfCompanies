from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from management_api.permissions import IsAdminOrWorkerReadOnly, OnlyCompanyAdmin, IsCompanyWorker
from management_api.models import Office
from management_api.serializers import BaseOfficeSerializer


class OfficeListCreateApiView(generics.ListCreateAPIView):
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (IsAdminOrWorkerReadOnly,)


class OfficeRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (OnlyCompanyAdmin,)
    lookup_field = 'id'


class ProfileOfficeRetrieveApiView(generics.GenericAPIView):
    permission_classes = (IsCompanyWorker,)
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer

    def get(self, request):
        instance = Office.objects.get(pk=request.user.office_id)
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)





