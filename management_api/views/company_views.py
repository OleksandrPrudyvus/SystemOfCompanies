from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from management_api.models import Company
from management_api.permissions import OnlyCompanyAdmin, IsNotWorker
from management_api.serializers import CompanySerializer


class CompanyCreateApiView(generics.GenericAPIView):
    queryset = Company
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated, IsNotWorker)

    def post(self, request, *args, **kwargs):
        if request.user.is_company_admin_user:
            return Response({'error': 'You already have a company'}, status=status.HTTP_409_CONFLICT)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        company_id = Company.objects.latest('id').id
        request.user.company_id = company_id
        request.user.is_company_admin_user = True
        request.user.is_worker = True
        request.user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CompanyRetrieveUpdateApiView(generics.GenericAPIView):
    serializer_class = CompanySerializer
    permission_classes = (OnlyCompanyAdmin,)

    def get(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializers = self.get_serializer(instance)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def put(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        instance = Company.objects.get(pk=request.user.company_id)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




