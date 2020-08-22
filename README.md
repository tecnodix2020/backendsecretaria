# Smart Desk BackEnd

The SmartDesk BackEnd is a back end for a virtual assistant desigend to automate a company's public service.

# New Features!

 ------------------

### Tech

Lisa Project uses a number of open source projects to work properly:

* [Python](https://www.python.org/) - Programming language
* [Django](https://www.djangoproject.com/) - Python web framework
* [MongoDB](https://www.mongodb.com/) - Cross-platform document-oriented database program, classified as a NoSQL database.
* [Djongo](https://pypi.org/project/djongo/) - Use Mongodb as a backend database for your django project, without changing a single django model!
* [django-cors-headers](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
* [django-rest-swagger](https://django-rest-swagger.readthedocs.io/en/latest/) - Swagger/OpenAPI Documentation Generator for Django REST Framework.
* [django-rest-framework-jwt](https://github.com/jpadilla/django-rest-framework-jwt) - JSON Web Token Authentication support for Django REST Framework.

### Installation

--------

### Plugins

-----------------------


### Development

------------

#### Building for source
---------

#### Kubernetes + Google Cloud

---------------------------


### Todos

 ------------

### Endpoints

#### Base URL: 
https://backendsecretaria.herokuapp.com/

#### Get Visits: 
https://backendsecretaria.herokuapp.com/visits

##### Possible parameters:
###### Types
Meeting = 1

Package = 2

General = 3

Example: https://backendsecretaria.herokuapp.com/visits?type=2

###### Visitor
The visitor personal code

Example: https://backendsecretaria.herokuapp.com/visits?visitor=12345678912

Observation: The visit is from the current day

#### Get the employees who are waiting for orders
https://backendsecretaria.herokuapp.com/packages/employees

##### Possible parameters:
###### Types
Meeting = 1

Package = 2

General = 3

Example: https://backendsecretaria.herokuapp.com/packages/employees?type=2

#### Get top 3 employees
https://backendsecretaria.herokuapp.com/visits/top3

##### Possible parameters:
###### Types
Meeting = 1

Package = 2

General = 3

Example: https://backendsecretaria.herokuapp.com/visits/top3?type=1

License
----

Not yet defined!