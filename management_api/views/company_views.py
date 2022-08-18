from rest_framework import generics
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from management_api.models import Company
from management_api.permissions import IsAdminOrWorkerReadOnly
from management_api.serializers import CompanySerializer


class CompanyCreateApiView(generics.CreateAPIView):
    queryset = Company
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class CompanyRetrieveUpdateApiView(generics.GenericAPIView):
    serializer_class = CompanySerializer
    permission_classes = (IsAdminOrWorkerReadOnly,)

    def get(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializers = self.get_serializer(instance)
        return Response(serializers.data)

    def put(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




