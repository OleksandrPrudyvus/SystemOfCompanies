from django.urls import path
from management_api import views

urlpatterns = [
    path('register/', views.UserRegisterApiView.as_view()),
    path('login/', views.LoginApiView().as_view()),
    path('company/', views.CompanyCreateApiView().as_view()),
    path('my-company/', views.CompanyRetrieveUpdateApiView().as_view()),
    path('my-company/workers/', views.WorkerListCreateApiView().as_view()),  # for company_admin
    path('my-company/workers/<int:id>/', views.WorkerRetrieveUpdateDestroyApiView().as_view(), name='worker_id'),  # for company_admin
    path('my-company/my-profile/', views.ProfileRetrieveUpdateApiView().as_view()),  # for workers
    path('my-company/office/', views.OfficeListCreateApiView().as_view()),  # for company_admin
    path('my-company/office/<int:id>/', views.OfficeRetrieveUpdateDestroyApiView().as_view(), name='retrieve_office'), # for company_admin
    path('my-company/my-profile/my-office', views.ProfileOfficeRetrieveApiView().as_view()),  # for workers
    path('my-company/vehicle/', views.VehicleListCreateApiView().as_view()), # for company_admin
    path('my-company/vehicle/<int:id>/', views.VehicleRetrieveUpdateDestroyApiView().as_view()),  # for company_admin
    path('my-company/my-profile/vehicle/', views.ProfileVehicleRetrieveApiView().as_view())  # for company_worker
]
