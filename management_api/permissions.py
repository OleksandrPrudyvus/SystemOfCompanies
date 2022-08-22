from rest_framework import permissions


class IsCompanyAdmin(permissions.BasePermission):
    """Provides company administrator rights"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_company_admin_user)


class IsCompanyWorker(permissions.BasePermission):
    """Provides rights only to company employees"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(request.user and request.user.is_worker)
        return False

    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_worker
            and obj.company_id == request.user.company_id
            and obj.office_id == request.user.office_id
        )


class OnlyCompanyAdmin(IsCompanyAdmin, permissions.BasePermission):
    """Provides model editing rights only to company administrators"""
    def has_object_permission(self, request, view, obj):
        return request.user.is_company_admin_user and obj.company_id == request.user.company_id


class IsAdminOrWorkerReadOnly(permissions.BasePermission):
    """
        Provides rights for models related to company_obj.
        If method Get, then it gives rights to everyone who is a worker.
        If methode (PUT or PATCH) is provided only to company administrators.

    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS and request.user.is_worker:
            return True
        return request.user.is_company_admin_user

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and \
                request.user.is_worker and request.user.company_id == obj.company_id:
                return True
        return request.user.is_company_admin_user and obj.company_id == request.user.company_id


class IsNotWorker(permissions.BasePermission):
    """Provides model editing rights only to  not company workers"""
    def has_permission(self, request, view):
        if request.user.is_worker:
            return False
        return True