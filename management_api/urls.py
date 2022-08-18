"""system_of_companies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from management_api import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('register/', views.UserRegisterApiView.as_view()),
    path('login/', obtain_auth_token),
    path('company/', views.CompanyCreateApiView().as_view()),
    path('my-company/', views.CompanyRetrieveUpdateApiView().as_view()),
    path('my-company/workers/', views.WorkerListCreateApiView().as_view()),  # for company_admin
    path('my-company/workers/<int:id>/', views.WorkerRetrieveUpdateDestroyApiView().as_view(), name='worker_id'),  # for company_admin
    path('my-company/my-profile/', views.ProfileRetrieveUpdateApiView().as_view()),  # for workers
    path('my-company/office/', views.OfficeListCreateApiView().as_view()),  # for company_admin
    path('my-company/office/<int:id>/', views.OfficeRetrieveUpdateDestroyApiView().as_view(), name='retrieve_office'), # for company_admin
    # path('my-company/my-profile/office', views.ProfileOfficeListApiView().as_view())  # for workers

    # path('my-company/vehicle/', views.VehicleListCreateApiView().as_view()) # for company_admin
    # path('my-company/vehicle/<int:id>/', views.VehicleRetrieveUpdateDestroyApiView().as_view()) # for company_admin

]
