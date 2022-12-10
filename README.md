# SystemOfCompanies

This is a web application that implements the display and management of a company through an API service.
# Role
1. CompanyAdmin. You can create, edit and delete a company. You can add, delete, view, change employees, offices and vehicles. Also, you can assign an employee to the office, and assign a vehicle to the employee. You can only know information about your company,  employees, offices and vehicle.

2. Worker. You can view your profile, your office, and vehicle.

***
# Technologies
 * Django/Django Rest Framework

### Start using the application
  * Docker must be installed
  * Docker-compose must be installed
### Deployment

1. Clone the repo: 
   
   * `https://github.com/OleksandrPrudyvus/SystemOfCompanies.git`

2. Run the app
  
  * `docker-compose up`
  * `docker-compose run web python3 manage.py migrate`
  * `docker-compose up`
  
***
##### After these steps you should see the home page of the application

***
# REST API
The REST API to the example app is described below.

# Implemented url paths:

### /register/
   * POST - Create new user.

### /login/
  * POST - Login user.

 ### /company/ 
  * POST - Create a company if you don't have any roles.

### /my-company/ 
  * GET - View your company.
  * PUT/PATCH - Change your company data if your role is CompanyAdmin.

### /my-company/workers/ - For CompanyAdmin.
  * GET - List of worker.
  * POST - Create new worker.

### /my-company/workers/<int:id>/ - For CompanyAdmin.
  * GET - Get worker.
  * PUT/PATCH - Change worker data.
  * DELETE - Delete worker.

### /my-company/my-profile/ 
  * GET - View your profile.
  * PUT/PATCH - Update your data.

### /my-company/office/ - For CompanyAdmin. 
  * GET - List of office.
  * POST - Create new office.

### /my-company/office/<int:id>/ - For CompanyAdmin. 
  * GET - Get office.
  * PUT/PATCH - Change office data.
  * DELETE - Delete office.
 
### /my-company/office/<int:id>/assign-worker/<int:wk_id>/ - For CompanyAdmin. 
  * POST - Assign worker in the office.

### /my-company/my-profile/my-office/ - For company Worker.
  * GET - View your office.

### /my-company/vehicle/ - For CompanyAdmin.
  * GET - List of vehicle.
  * POST - Create new vehicle.

### /my-company/vehicle/<int:id>/ - For CompanyAdmin.
  * GET - View of vehicle.
  * PUT/PATCH - Change vehicle data.
  * DELETE - Delete vehicle.

### /my-company/my-profile/vehicle/ - For company Worker.
  * GET - List of employee's vehicle.
