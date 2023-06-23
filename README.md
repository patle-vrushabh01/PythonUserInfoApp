# Overview
The application is developed in Python Flask Framework. The application will have 4 apis for create,update,delete,get
customers from a json file

# Installation steps
open terminal and go to "Python_sample_project" directory. After that, run following command
pip install -r requirements.txt

Run the application using below command
flask run

# Open browser and visit http://localhost:5000/apidocs
To add new API and it's swagger definition
To define an API, write your api in routes.py and create an associate swagger specification in swagger directory. To
link the API with the swagger specification, you can use the "swag_from" function. See below. After that you can see
your api in swagger UI i.e /apidocs

@api.route(<api_url>)
@swag_from("../swagger/<name_of_yaml_file>)
def handler_method(..): ....

# Swagger
To see all swagger specification you can follow the below link

https://swagger.io/docs/specification/basic-structure/

# Directories

Config
This folder keeps all configuration swagger
# Deployment with Waitress (Windows)
Note: Make sure to run all pip commands in the application virtualenv to isolate the project specific installation from
outside environment

Open terminal and go to project root directory "flask_swagger_starter"
Activate the virtualenv by running below command in terminal
venv/scripts/activate

Install project dependencies if not installed
pip install -r requirements.txt

Install waitress
pip install waitress

Run application with waitress-serve
waitress-serve --host 127.0.0.1 --port=5000 wsgi:app

--host : binds the server to local 127.0.0.1
--port : binds port number
wsgi:app : "wsgi" refers to wsgi.py where the "app" (flask app) object is created. It provide the flask "app" instance
to waitress server.