"""This module is designed to reduce code duplication"""
from management_api.models import User


class GetUserCompanyMixin:
    """MixinClass that provides the current company"""
    def save(self, **kwargs):
        self.company = self.context.get('request').user.company
        kwargs['company'] = self.company
        super().save(**kwargs)


class CheckUserIsOfficeStaffMixin:
    """MixinClass that checks whether an employee is an office employee"""
    def check_office_staff(self, request, *args, **kwargs):
        if request.data.get('office', False) and request.data.get('user', False):
            office_instance = request.data.get('office')
            user_list_instances = request.data.get('user')
            for i in user_list_instances:
                if User.objects.get(pk=i).office_id != office_instance:
                    return False
        return True


class CurrentCompanyDefault:
    """MixinClass that provides the current company, for serializer_field"""

    def set_context(self, serializer_field):
        self.company = serializer_field.context['request'].data.get('company')

    def __call__(self):
        return self.company

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CurrentUsernameDefault:
    """MixinClass that provides the current name, for serializer_field"""
    def set_context(self, serializer_field):
        self.data = serializer_field.context['request'].data
        self.username = str(self.data.get('first_name'))+str(self.data.get('last_name'))

    def __call__(self):
        return self.username

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class CheckConfirmPasswordMixin:
    """MixinClass that provides password validation"""

    def check_confirm_password(self, request) -> bool:
        password = request.data.get('password')
        repeat_password = request.data.get('repeat_password')
        if password == repeat_password:
            return True
        return False
