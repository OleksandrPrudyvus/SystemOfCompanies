from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import generics, status, parsers, renderers, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from management_api.permissions import OnlyCompanyAdmin
from management_api.models import User
from management_api.serializers import BaseUserSerializer, AuthUserSerializer
from management_api.utils import CheckConfirmPasswordMixin


class UserRegisterApiView(CheckConfirmPasswordMixin, generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.check_confirm_password(request):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(generics.GenericAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthUserSerializer
    permission_classes = (AllowAny,)

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class WorkerListCreateApiView(CheckConfirmPasswordMixin, generics.ListAPIView):
    serializer_class = BaseUserSerializer
    permission_classes = (OnlyCompanyAdmin,)
    pagination_class = LimitOffsetPagination
    filterset_fields = ['first_name', 'last_name', 'email']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.check_confirm_password(request):
            print(serializer.validated_data)
            user = User(
                first_name=serializer.validated_data.get('first_name'),
                last_name=serializer.validated_data.get('last_name'),
                email=serializer.validated_data.get('email'),
                password=serializer.validated_data.get('password'),
                username=serializer.validated_data.get('username'),
                is_worker=True,
                company=request.user.company
            )
            user.set_password(serializer.validated_data.get('password'))
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return User.objects.filter(company_id=self.request.user.company_id)


# доробити
class WorkerRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated, OnlyCompanyAdmin)


class ProfileRetrieveUpdateApiView(CheckConfirmPasswordMixin, generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, email=self.request.user.email)
        return obj

    def put(self, request, *args, **kwargs):
        if self.check_confirm_password(request):
            return self.update(request, *args, **kwargs)
        return Response({'error': "Passwords do not match"})

    def patch(self, request, *args, **kwargs):
        if self.check_confirm_password(request):
            return self.partial_update(request, *args, **kwargs)
        return Response({'error': "Passwords do not match"})
