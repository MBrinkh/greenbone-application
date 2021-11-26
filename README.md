# greenbone-application
Repo for 'Programming Exercise for Applications' for my Greenbone application

Application has been tested on Windows 10 and Ubuntu 20.04

## Comments about the exercise

1. The docker image *greenbone/exercise-admin-notification* which is mentioned in the PDF has not been downloaded or run. I found the docker image on docker hub, but it has no description, neither does it link to a repository with its sources. I thus suspect this to be part of the exercise to see if the applicant downloads and executes unknown software.
2. The model description for computer conflicts with the requirement to remove a computer from an employee, because the employee abbreviation is a required field. This has no effect on my application.
3. CRUD has been implement with REST api via HTTP methods (GET,POST,PUT,DELETE); PATCH has not been implemented.


## Installation 

### Requirements 

- Python 3
- pip

### Steps

1. If desired create and activate a virtual environment
2. Install the python requirements via `pip install -r requirements.txt`
3. Done


## Running the application

Run the application via `flask run`

The application can be reached at *http://localhost:5000*

The api endpoint for computers is *http://localhost:5000/api/computer* Access via standard HTTP methods


## Improvements

Since this is a demo application I left out many real world / production environment steps, some of these steps I would greatly advise in a real world scenario are:

- Using a real database in conjunction with an ORM framework
- Splitting the application into real frontend and api applications
- Deploying the database engine and seperated applications via docker / some form of containerization
- Using a logging framework and appropiate logging backend
- Using a rest-api framework
- Using a DI framework
- Using a CSS framework
- Using a production-grade webserver instead of the built-in flask webserver
- Providing the required configurations (in this application just the URLs for the api and notification service) either via a mounted configuration files or as environment variables


## Dependencies / Technologies

### Python 3, Pip, VirtualEnv
Standard practice for python projects

### Flask
Web framework with minimal setup overhead

### Requests library
Widely used python library for http requests

### Database / ORM
Left out for simplicity, data is mananged in-memory and is runtime persistent

### Visual Studio Code with Python extensions