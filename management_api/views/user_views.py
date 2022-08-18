from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from management_api.permissions import IsCompanyWorker, OnlyCompanyAdmin
from management_api.models import User
from management_api.serializers import WorkerUserSerializer, BaseUserSerializer


class WorkerListCreateApiView(generics.GenericAPIView):
    serializer_class = WorkerUserSerializer
    permission_classes = (IsAuthenticated, OnlyCompanyAdmin)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(company_id=request.user.company_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = WorkerUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create(
            username=request.data.get('username'),
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            password=request.data.get('password'),
            repeat_password=request.data.get('repeat_password'),
            email=request.data.get('email'),
            company_id=request.user.company_id,
            is_worker=True
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return User.objects.all()

# доробити
class WorkerRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated, OnlyCompanyAdmin)


class ProfileRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = (IsAuthenticated, IsCompanyWorker)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, username=self.request.user)
        return obj
