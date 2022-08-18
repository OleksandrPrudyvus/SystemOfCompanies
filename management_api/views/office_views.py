from rest_framework import generics, status
from rest_framework.response import Response
from management_api.permissions import IsAdminOrWorkerReadOnly, OnlyCompanyAdmin, IsCompanyWorker
from management_api.models import Office
from management_api.serializers import BaseOfficeSerializer

class OfficeListCreateApiView(generics.CreateAPIView):
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (IsAdminOrWorkerReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().filter(company_id=request.user.company_id))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OfficeRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (OnlyCompanyAdmin,)
    lookup_field = 'id'


class ProfileOfficeRetrieveApiView(generics.GenericAPIView):
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (IsCompanyWorker,)

    def get(self, request):
        instance = Office.objects.get(pk=request.user.office_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)





