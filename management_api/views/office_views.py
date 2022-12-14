from rest_framework import generics, response, status
from rest_framework.permissions import IsAuthenticated
from management_api.permissions import OnlyCompanyAdmin, IsCompanyWorker, IsAdminOrWorkerReadOnly
from management_api.models import Office, User
from management_api.serializers import BaseOfficeSerializer


class OfficeListCreateApiView(generics.ListCreateAPIView):
    """ApiView to get(list) and create Office, accepts GET, POST method"""
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (IsAdminOrWorkerReadOnly,)
    filterset_fields = ['country', 'city']

    def get_queryset(self):
        return Office.objects.filter(company_id=self.request.user.company_id)


class OfficeRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    """ApiView to get and change Office, accepts GET, PUT, PATCH method"""
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (OnlyCompanyAdmin,)
    lookup_field = 'id'


class ProfileOfficeRetrieveApiView(generics.ListAPIView):
    """ApiView to get worker's Office, accepts GET method"""
    queryset = Office.objects.all()
    serializer_class = BaseOfficeSerializer
    permission_classes = (IsCompanyWorker,)

    def get_queryset(self):
        return Office.objects.filter(pk=self.request.user.office_id)


class AssignWorkerApiView(generics.GenericAPIView):
    """ApiView to appoint an employee to the office, accepts POST method"""
    permission_classes = (IsAuthenticated, OnlyCompanyAdmin,)
    queryset = Office.objects.all()

    def post(self, request, *args, **kwargs):
        current_user = User.objects.get(pk=kwargs['wk_id'])
        current_office = Office.objects.get(pk=kwargs['id'])

        if current_office.company == current_user.company:
            current_user.office_id = current_office.pk
            current_user.save()
            return response.Response(
                {'msg': f'The user {current_user} is now an office worker'},
                status=status.HTTP_200_OK
            )
        return response.Response(
            {'msg': 'The user is not an employee of the company'},
            status=status.HTTP_400_BAD_REQUEST
        )


