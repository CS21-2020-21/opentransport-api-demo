# TP3 - CS21 Main
[![pipeline status](https://stgit.dcs.gla.ac.uk/tp3-2020-CS21/cs21-main/badges/master/pipeline.svg)](https://stgit.dcs.gla.ac.uk/tp3-2020-CS21/cs21-main/-/commits/master)[![coverage report](https://stgit.dcs.gla.ac.uk/tp3-2020-CS21/cs21-main/badges/master/coverage.svg)](https://stgit.dcs.gla.ac.uk/tp3-2020-CS21/cs21-main/-/commits/master)

Main code repository for Team Project 3 of Honours program.

# Project

[Open Transport Initiative](https://opentransport.co.uk/)

There are two components to our project:

* Implementing the Customer-Account API Specification, providing a proof of concept to demonstrate the interaction between two customer accounts.  We are creating mock accounts to act as endpoints and illustrate how the API facilitates communication of customer data between them.

* Implementing the Centralised Operator-Info API, providing  a lookup service which makes use of the PAS 212 standard in order to retrieve the details of different transport operators and MaaS platforms.  We are creating a simple endpoint to act as a query tool, where transport operators have the opportunity to fetch company data from the centralised database.

# Built With


* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Bootstrap](https://getbootstrap.com/)



# Contributors

* [Ans Farooq](mailto:2390370f@student.gla.ac.uk) - 2390370f
* [Dominykas Meistas](mailto:2404288m@student.gla.ac.uk) - 2404288m
* [Pragati Mishra](mailto:2506109m@student.gla.ac.uk) - 2506109m
* [David O'Neill](mailto:2378524o@student.gla.ac.uk) - 2378524o
* [Lewis Tse](mailto:2385606t@student.gla.ac.uk) - 2385606t

## Coach

* Beth McDermid

# Installation

* Clone the repository:
```shell
$ git clone https://stgit.dcs.gla.ac.uk/tp3-2020-CS21/cs21-main.git
$ cd cs21-main
```
* Create and activate your virtual environment


## Centralised Operator Database
* Perform the following commands
```shell
(env_name)$ cd ProjectImplementation/APIs/operator_api
(env_name)$ pip install -r requirements.txt
(env_name)$ python manage.py makemigrations api
(env_name)$ python manage.py migrate
(env_name)$ python populate.py
(env_name)$ python manage.py runserver
```
* Now navigate to http://127.0.0.1:8000/


## Operator Database Query Tool
* Perform the following commands
```shell
(env_name)$ cd ProjectImplementation/QueryTools/operators_query_tool
(env_name)$ pip install -r requirements.txt
(env_name)$ python manage.py makemigrations
(env_name)$ python manage.py migrate
(env_name)$ python manage.py runserver
```
* Now navigate to http://127.0.0.1:8000/

## Customer Account Query Tool
* Perform the following commands
```shell
(env_name)$ cd ProjectImplementation/QueryTools/customer_query_tool
(env_name)$ pip install -r requirements.txt
(env_name)$ python manage.py makemigrations customers
(env_name)$ python manage.py migrate
(env_name)$ python populate.py
(env_name)$ python manage.py runserver
```
* Now navigate to http://127.0.0.1:8000/index

## Second Customer Account Query Tool
* Perform the following commands
```shell
(env_name)$ cd ProjectImplementation/QueryTools/second_customer_query_tool/customer_query_tool
(env_name)$ pip install -r requirements.txt
(env_name)$ python manage.py makemigrations customers
(env_name)$ python manage.py migrate
(env_name)$ python populate.py
(env_name)$ python manage.py runserver
```
* Now navigate to http://127.0.0.1:8000/index

# Usage

## Centralised Operator Database

This is a centralised database storing details of transport operators and modes.  It is an implementation of the Open Transport Initiative Centralised Operator-info API, conforming to the specification.  This is not designed to be used, and the code provided is simply an example of what is required to implement the API specification.  
For more details, go to:<br/>
[Centralised Operator-info API Documentation](https://app.swaggerhub.com/apis/open-transport/operator-info/1.1.0)</br>
This web application has been hosted at:</br>
https://cs21operatorapi.pythonanywhere.com

## Operator Database Query Tool

This web application is designed to be used as a way of querying the centralised operator database.  It provides a means for the user to perform all the necessary queries on the database to match the specification.  To use, register and account, click to get started and begin performing queries.  This tool is not hosted remotely, but can be run on the Django development server in order to query the pythonanywhere hosted operator database.

## Customer Account Query Tool

This web application is a mock transport operator's account.  You can register for a fake user account, check any purchases you have made on this website and also link to your account on other websites.  When linking to another user account, the email verification is currently disabled.  Instead, the verification code is always "123456".  Once you have linked to another account, it is possible to check your details of the other account.  The linked accounts should exchange data using the Open Transport Customer-account specification.</br></br>
After running the command line instructions above, the database will be populated with 5 mock users who have already got data, with usernames 1-5.  The password for each user is "12345678abc".</br></br>
This web application is not hosted remotely, but can be run on the Django development server.  The second customer account called PSDBuses is hosted on pythonanywhere, allowing your local machine to query the remotely hosted machine, demonstrating the communication between two accounts.  The remote PSDBuses account has the same 5 users with the data on each of them, so linking to a user on PSDBuses with username 1-5 will illustrate the flow of data.  For more information, go to:</br>
[Customer-account API Documentation](https://app.swaggerhub.com/apis/open-transport/customer-account/)


## Second Customer Account Query Tool

This web application performs the same function as the first customer query tool.  It is simply a different mock transport operator website, so that the two can communicate.  This web application is hosted at:</br>
https://psdbuses.pythonanywhere.com/index/

# Testing

## Operator Query Tool
There are unit and integration tests for the operators query tool, making use of coverage.  In order to run the tests and evaluate the coverage, two consoles must be open.  The first should run the operators query tool using the running instructions above.  The Django development server should be kept running.  In the second console, perform the following commands:
```shell
(env_name)$ cd ProjectImplementation/QueryTools/operators_query_tool
(env_name)$ coverage erase
(env_name)$ coverage run manage.py test operators
(env_name)$ coverage report
```

## Customer Query Tool
There are unit and integration tests for the customer query tool, making use of coverage.  In order to run the tests and evaluate the coverage, two consoles must be open.  The first should run the customer query tool using the running instructions above.  The Django development server should be kept running.  In the second console, perform the following commands:
```shell
(env_name)$ cd ProjectImplementation/QueryTools/customer_query_tool
(env_name)$ coverage erase
(env_name)$ coverage run manage.py test customers
(env_name)$ coverage report
```
## Customer API and Operator API
### Postman Testing
In Postman, click the Runner button at the top of the Postman window. The Collection Runner window will appear.
Under "Choose a collection or folder", select the folder containing the collection to run.
Click the Environment menu and choose the environment to use.
Click the Start Run button.


# Releases


This repository makes use of release branching, with feature branching off of each release branch.  Currently, there are four releases of our project with the fifth release in development.


# Roadmap

Our repository is currently undergoing intensive testing and refactoring to deliver to our customer.  We will be storing our proof of concept on a GitHub repository to pass the code onto our customer and also act as a guide for developers implementing the API specifications in the future.

# Credits

* This project is an implementation of the [Open Transport Initiative Open Standard API specifications](https://opentransport.co.uk/open-standard/)

# License

[TBC]()