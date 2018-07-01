# Animal backend api using Django

Each Animal instance has 5 key value pairs: id, commonName, scientificName, family, imageURL

The api has one basic url /Animal/

# Routes

GET - http://127.0.0.1:8000/Animal/
Returns all Animal instances from the database

GET by id http://127.0.0.1:8000/Animal/(id)
Returns Animal instance with matching id

POST http://127.0.0.1:8000/Animal/
Saves Animals data to the database, expects the key value pairs: commonName, scientificName, family, imageURL in the body of the request.  

PUT http://127.0.0.1:8000/Animal/(id)
Updates the Animal in the database, expects the key value pairs: commonName, scientificName, family, and imageURL in the body of the request.

DELETE http://127.0.0.1:8000/Animal/(id)
Deletes Animal from the database with the corrresponding ID

## SETUP INSTRUCTIONS
 * Clone or download this repository
 * navigate to the root directory via terminal
 * Set up a virtual env 
    $ virtualenv ENV
 * Navigate into ENV file and run command
    $ source bin/activate
 * Navigate back to root directory and install dependencies into virtual env
    pip install django
    pip install djangorestframework
 * Make initial Migration of Animal Model and sync database, First navigate into the nevelex_animals folder and run commands
    python manage.py makemigrations animals_api
    python manage.py migrate
 * Run Server
    python manage.py runserver

You can now interact with the backend api

