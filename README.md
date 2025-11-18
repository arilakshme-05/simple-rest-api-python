#  Simple REST API using Flask

This project is a basic REST API built with Flask.  
It supports *GET, **POST, **PUT, and **DELETE* operations for demonstration and testing in Postman or curl.

## Features
- Simple and clean REST API structure  
- Supports JSON request + response  
- Works with Postman & curl  
- Handles 415 errors by requiring proper Content-Type  

##  API Endpoints

### *GET /users*
Returns all users.
GET http://127.0.0.1:5000/users
###  *POST /users*
Creates a new user.

 *Headers (IMPORTANT)*

Content-Type: application/json

 *Body (raw → JSON)*
```json
{
  "id": 1,
  "name": "Ari",
  "age":25
}

Response

{
  "message": "User created successfully",
  "user": { ... }
}
### *PUT /users/<id>*

Updates a user.

{
  "name": "Updated Name"
}

### DELETE /users/<id>

Deletes a user

