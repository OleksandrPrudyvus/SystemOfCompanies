"""This module is designed to reduce code duplication"""


class GetUserCompanyMixin:
    def save(self, **kwargs):
        self.company = self.context.get('request').user.company
        kwargs['company'] = self.company
        super().save(**kwargs)

