from .user_views import (
    UserRegisterApiView,
    ProfileRetrieveUpdateApiView,
    WorkerListCreateApiView,
    LoginApiView,
    WorkerRetrieveUpdateDestroyApiView)

from .office_views import (
    AssignWorkerApiView,
    OfficeListCreateApiView,
    ProfileOfficeRetrieveApiView,
    OfficeRetrieveUpdateDestroyApiView
)
from .company_views import CompanyCreateApiView, CompanyRetrieveUpdateApiView
from .vehicle_views import VehicleListCreateApiView, VehicleRetrieveUpdateDestroyApiView, ProfileVehicleRetrieveApiView

"""Module for import views"""

