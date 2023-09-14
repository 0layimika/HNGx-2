# API Documentation
# Overview
This document provides an overview of the API structure and key components of the API. It is pertinent to note that this API was created with the assumption that more than a person can have the same name and details, they are differentiated by an automatically generated id(pk). Therefore, a person can be called using the id for the person as it is the only field that is different for all persons. Once a person is called by the id, all CRUD operations would be able to be performed on the person.
# Getting Started
To run the API locally, follow these steps:
### Prerequisite:
- Python and Django must be installed most importantly</li>
- Refer to requirements.txt for other required installations</li>
## Running the API
- Run the start command : Python manage.py runserver
## Folder Structure

The API project has the following folder structure. It is important this outlines only the vital files and folders responsible for the running of the API: 
- `person_api`
  - `Settings.py`:contains all the settings of the entire running of the api
- `api`
  - `apps.py`: Configuration file
  - `serializer.py`: Responsible for the serializing and deserializing of the database objects
  - `models.py`: Data Models
  - `views.py`: API endpoints/functions
  - `urls.py`: Url patterns
- `manage.py` : Main entry point
- `db.sqlite3` : Database and it's command

## `manage.py`
The `manage.py` file is the main entry point and it holds all the command to be performed on the server. It initializes the sqlite3 connection and starts the HTTP server.

## `views.py`

The `views.py` folder contains HTTP request handler functions for managing Person resources. It includes functions for creating, retrieving, updating, and deleting Person objects.

- `personlistcreateview`: Creates a new Person.
- `persondetailview`: Retrieves a Person by id, updates an existing person and also deletes a person by id

The `models.py` folder defines the data structure for a Person and provides database-related functionality.

- `Person`: Represents a Person resource.

## Conclusion

This documentation provides an overview of the structure and key components of the API. For more detailed information on each component and their functions, refer to the corresponding source code files in the repository.
