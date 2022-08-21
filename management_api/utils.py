"""This module is designed to reduce code duplication"""
from management_api.models import User


class GetUserCompanyMixin:
    def save(self, **kwargs):
        self.company = self.context.get('request').user.company
        kwargs['company'] = self.company
        super().save(**kwargs)


class CheckUserIsOfficeStaffMixin:
    def check_office_staff(self, request, *args, **kwargs):
        if request.data.get('office', False) and request.data.get('user', False):
            office_instance = request.data.get('office')
            user_list_instances = request.data.get('user')
            for i in user_list_instances:
                if User.objects.get(pk=i).office_id != office_instance:
                    return False
        return True


class CheckOfficeIsCompanyPropertyMixin:
    def check_company_property(self, request, *args, **kwargs):
        pass


class CurrentUsernameDefault:
    def set_context(self, serializer_field):
        self.data = serializer_field.context['request'].data
        self.username = str(self.data.get('first_name'))+str(self.data.get('last_name'))

    def __call__(self):
        return self.username

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CheckConfirmPasswordMixin:

    def check_confirm_password(self, request) -> bool:
        password = request.data.get('password')
        repeat_password = request.data.get('repeat_password')
        if password == repeat_password:
            return True
        return False
