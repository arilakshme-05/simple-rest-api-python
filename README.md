# Simple REST API using Flask

A lightweight RESTful API built with Python Flask demonstrating standard CRUD (`GET`, `POST`, `PUT`, `DELETE`) operations, JSON payload handling, and error validation.

---

##  Features

* **RESTful Architecture:** Clean separation of HTTP methods for resource management.
* **JSON Request & Response:** Accepts and returns structured JSON payloads.
* **Error Handling:** Validates request headers and returns `415 Unsupported Media Type` if `Content-Type: application/json` is missing.
* **API Testing Ready:** Fully compatible with Postman, Insomnia, and `curl`.

---

##  Tech Stack

* **Language:** Python 3
* **Framework:** Flask

---

##  API Endpoints

### 1. `GET /users`
Retrieves a list of all registered users.

* **URL:** `http://127.0.0.1:5000/users`
* **Method:** `GET`

---

### 2. `POST /users`
Creates a new user record.

* **URL:** `http://127.0.0.1:5000/users`
* **Method:** `POST`
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "id": 1,
    "name": "Ari",
    "age": 25
  }
Success Response:
JSON
{
  "message": "User created successfully",
  "user": {
    "id": 1,
    "name": "Ari",
    "age": 25
  }
}

3. PUT /users/<id>
Updates an existing user's information by ID.

URL: http://127.0.0.1:5000/users/1

Method: PUT

Headers: Content-Type: application/json

Request Body:

JSON
{
  "name": "Updated Name"
}

4. DELETE /users/<id>
Deletes a user record by ID.

URL: http://127.0.0.1:5000/users/1

Method: DELETE

How to Run:
1.Clone the repository:
git clone [https://github.com/arilakshme-05/flask-rest-api.git](https://github.com/arilakshme-05/flask-rest-api.git)
cd flask-rest-api

2.Install dependencies:
pip install flask

3.Run the API server:
python app.py

4.Test with curl:
curl -X GET [http://127.0.0.1:5000/users](http://127.0.0.1:5000/users)
