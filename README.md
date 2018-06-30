Animal backend api using Django

Each Animal instance has 5 key value pairs: id, commonName, scientificName, family, imageURL

The api has one basic url /Animal/

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
