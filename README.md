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
