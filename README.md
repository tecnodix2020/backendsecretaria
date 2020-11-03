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

### Building for source
---------

### Todos

 ------------

### Endpoints

#### Base URL: 
https://backendsecretaria.herokuapp.com/

#### Authentication:
https://backendsecretaria.herokuapp.com/auth
##### Type Request
AUTH
##### Body
```sh
{
    "username": "gferreira",
    "password": "12345678"
}
```

#### Get Visits: 
https://backendsecretaria.herokuapp.com/visits

##### Possible parameters:
###### Types
Meeting = 1

Package = 2

General = 3

Example: https://backendsecretaria.herokuapp.com/visits?type=2

#### Post Visits: 
https://backendsecretaria.herokuapp.com/api/visits

##### Type Request
POST
##### Body
```sh
{
    "idEmployee": "44a7b571-47d6-438e-8c7b-34c1094d0d5a",
    "idTypeVisit": "2",
    "dateVisit": "2020-08-05",
    "subs": [
        "1ef6fda7-d153-498e-8d25-1addb50c5dd9",
        "44a7b5c8-47d6-438e-8c7b-34c1094d0d5a"
    ]
}
```

Example: https://backendsecretaria.herokuapp.com/api/visits

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

#### Get Employees
https://backendsecretaria.herokuapp.com/employees
##### Possible parameters:
###### Name

Any name or piece of name (It is not case-sensitive)

Examples: https://backendsecretaria.herokuapp.com/employees?name=guilherme

https://backendsecretaria.herokuapp.com/employees?name=vas

### Store Users
https://backendsecretaria.herokuapp.com/users

##### Type Request
POST
##### Body
```sh
{
    "name": "Felipe Freitas",
    "email": "ffreitas@getmail.com.br",
    "username": "ffreitas"
}
```

### Get User
https://backendsecretaria.herokuapp.com/users/:id

##### Type Request
GET

Example: https://backendsecretaria.herokuapp.com/users/518a69e3-0110-404f-8047-4a59ceef1d8d

### Store Visitor
https://backendsecretaria.herokuapp.com/visitors

##### Type Request
POST
##### Body
```sh
{
    "personalCode": "12345678913",
    "idCompany": "f556895f-efa3-4428-b6a5-f90dd7e3a94e",
    "name": "Italo Gomes",
    "email": "italo@gmail.com",
    "observation": "Nenhuma observação"
}
```

### Get Visitor
https://backendsecretaria.herokuapp.com/visitors/:id

##### Type Request
GET

Example: https://backendsecretaria.herokuapp.com/visitors/08dc50d5-49b8-467e-a4fd-720d14d230a2


License
----

Not yet defined!