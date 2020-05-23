# Full Stack API Final Project

## Full Stack Casting Agency

This project is the final project of the Udacity Full Stack Developer Nano Degree. The goal of this project is to deploy a Flask application with Heroku/PostgreSQL and enable Role Based Authentication and roles-based access control git (RBAC) with Auth0 (third-party authentication systems).

I decided to implement a RESTful for a Casting Agency app where that is responsible for creating movies and managing and assigning actors to those movies.

Roles:
1. Casting Assistant
2. Casting Director
3. Executive Producer

## Getting Started

### Pre-Requisites

Create postgre database for running Unit tests

## About the Stack

### Backend

The project is deployed in Heroku.
Role based authentication has been setup for 3 roles using AUTH0

### Endpoint for testing 

https://capstone-app-shalini.herokuapp.com/

### Unit Tests

1. To run the tests locally, make sure you have PostgreSQL installed, https://www.postgresql.org/
2. Create a test postgre database.
3. Setup the environment variables as mentioned in config_settings.env file
    a. DATABASE_URL - Update the datatabase name, user name, password
    b. TOKEN_TEST - Set up this value as it is. This is the Bearer token generated from AUTH0 for the roles - Executive Producer
4. After setting up environment variables, run the below command. Make sure you are in the folder where test_app.py file is present.

```bash
python test_app.py
```
Note: Run the test only after setting up the environment variables correctly so that all tests will be successful in first attempt. Else, you may have to update the ID field of tables accordingly. 

### Test using Postman

1. Authorization token for all roles has been updated in postman collection file - Capstone.postman_collection
2. Import this postman collection file in POSTMAN app and run all cases
3. Alternatively, use newman to run postman collection

```bash
newman run Capstone.postman_collection.json
```

## API Reference

### Getting Started

1. Base URL : Backend app is hosted on https://capstone-app-shalini.herokuapp.com/
2. Authentication : Role based authentication using AUTH0

### Error Handling

Errors are returned as JSON objects in the following format:

{
    "success": False, 
    "error": 404,
    "message": "Resource Not Found"
}

The API will return these error types when requests fail:
400: bad request
404: Resource not found
422: unprocessable
500: Internal Server Error

If the route requires authentification and the request fails, it will return:
401: "authorization_header_missing"
400: "invalid_claims"
403: "unauthorized"

### Roles and Permissions

#### Casting Assistant 
• Can view actors and movies

#### Casting Director 
• All permissions a Casting Assistant has and… 
• Add or delete an actor from the database 
• Modify actors or movies

#### Executive Producer
• All permissions a Casting Director has and… 
• Add or delete a movie from the database

### Endpoints

#### GET /

No authentication required. This will return

{
    "Message": "Welcome to Casting Agency App"
}

#### GET /actors (Auth required)

Returns details of all actors. Sameple output below. 

{
    "actors": [
        {
            "age": 25,
            "gender": "female",
            "id": 1,
            "name": "Dany"
        },
        {
            "age": 26,
            "gender": "female",
            "id": 45,
            "name": "actor name ep 3"
        }
    ],
    "success": true
}

#### GET /actors/<actor_id> (Auth required)

Returns actor details for the given id. Sameple output below. 

{
    "actors": {
        "age": 25,
        "gender": "female",
        "id": 1,
        "name": "Dany"
    },
    "success": true
}

#### GET /movies (Auth required)

Returns details of all movies. Sameple output below. 

{
    "movies": [
        {
            "id": 1,
            "releasedate": "20-07-2015",
            "title": "Frozen"
        },
        {
            "id": 42,
            "releasedate": "16-09-2019",
            "title": "Movie name 3"
        }
    ],
    "success": true
}

#### GET /movies/<movie_id> (Auth required)

Returns movies details for the given id. Sameple output below. 

{
    "movies": {
        "id": 1,
        "releasedate": "20-07-2015",
        "title": "Frozen"
    },
    "success": true
}

#### POST /actors (Auth required)

Add new actor. Sample JSON input below

{
	"name": "John",
	"age": "26",
	"gender": "male"
}

#### POST /movies (Auth required)

Add new movie. Sample JSON input below

{
	"title": "Toy Story",
	"releasedate": "20-07-2015"
}

#### PATCH /actors/<actor_id> (Auth required)

Update existing actor. Sample JSON input below

{
	"name": "Dany",
	"age": "25"
}

#### PATCH /movies/<movie_id> (Auth required)

Update existing movie. Sample JSON input below

{
	"title": "Frozen"
}

#### DELETE /actors/<actor_id> (Auth required)

Delete existing actor. Sample Output below

{
    "deleted_actor_id": 35,
    "message": "Actor successfully deleted!",
    "success": true
}

#### DELETE /movies/<movie_id> (Auth required)

Delete existing movie. Sample Output below

{
    "deleted_movie_id": 34,
    "message": "Movie successfully deleted!",
    "success": true
}

### AUTHORS

Shalini Thangappazham

## Acknowledgements

I want to thank Udacity for providing the framework and guidelines for this great project.
