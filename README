# CARFORD SYSTEM API

This is a simple RESTful API for the following challenge:

```
Nork-Town is a weird place. Crows cawk the misty morning while old men squint. It’s a small
town, so the mayor had a bright idea to limit the number of cars a person may possess. One
person may have up to 3 vehicles. The vehicle, registered to a person, may have one color,
‘yellow’, ‘blue’ or ‘gray’. And one of three models, ‘hatch’, ‘sedan’ or ‘convertible’.
Carford car shop want a system where they can add car owners and cars. Car owners may
not have cars yet, they need to be marked as a sale opportunity. Cars cannot exist in the
system without owners.
```

The challenge was to build a simple RESTful API for managing car owners and their cars. The API had to be built using Python and Flask, and it needed to allow users to create, read, update, and delete owners and cars.


### The challenge had the following requirements:

- Setup the dev environment with docker
- Using docker-compose with as many volumes as it takes
- Use Python’s Flask framework and any other library
- Use any SQL database
- Secure routes
- Write tests

### And the following rules:

- The vehicle, registered to a person, may have one color,‘yellow’, ‘blue’ or ‘gray’
- The vehicle, registered to a person may have one of three models, ‘hatch’, ‘sedan’ or ‘convertible’
- Cars cannot exist in the system without owners.
- One person may have up to 3 vehicles.

Overall, the challenge aimed to assess the candidate's ability to design and implement a simple RESTful API that met a specific set of requirements, as well as their ability to write clean and well-documented code and their skill in writing effective unit tests.



## Overview

This RESTful API allows you to manage car owners and their cars.  You can create, read, update, and delete owners and their cars.
The project is built using Python, Flask framework, SQLAlchemy and utilizes JWT for authentication. It also uses Docker for containerization and Flask-Migrate for database migrations.


## Getting Started

1. Clone this repository: 

```
git clone https://github.com/kalelmartinho/carford-api.git
```

2. Create a virtual environment:

```
python venv venv
```

3. Activate the virtual environment

Windows:
```
./venv/Scripts/Activate.ps1
```
Linux or Unix:
```
source venv/bin/activate
```

4. Install the required packages:

```
pip install -r requirements.txt
```

5. Create the database tables using Flask-Migrate: 

```
flask db init
flask db migrate
flask db upgrade
``` 

6. Build the docker image:

```
docker-compose build
```

7. Start the Docker container:

```
docker-compose up
```

-The application should now be running at http://localhost:5000.


## Tests

You can run the tests by

1. Installing pytest:

```
pip install pytest
```

2. run pytest in terminal

```
pytest
```

## Authentication

All API endpoints require authentication using a JWT token.

| Endpoint                            | HTTP Method | Result                                     |
| ----------------------------------- | -----------| ------------------------------------------ |
| /auth/register                      | POST       | Register a new user                 |
| /auth/login                         | POST       | Get a Bearer token                  |

To obtain a token, send a POST request to /api/auth/login with a JSON body containing your username and password. For example:

```
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

If the credentials are correct, the API will respond with a JSON object containing the token. For example:

```
{
  "access_token": "yourjwttoken"
}
```

Include this token in the Authorization header of all subsequent requests. For example:


```
{
  "Authorization": "Bearer yourjwttoken"
}
```

## API Endpoints

### Owners

| Endpoint                            | HTTP Method | Result                                     |
| ----------------------------------- | -----------| ------------------------------------------ |
| /api/owners                         | GET        | Get all owners                             |
| /api/owners/<int:owner_id>          | GET        | Get a single owner by ID                   |
| /api/owners                         | POST       | Create a new owner                         |
| /api/owners/<int:owner_id>          | PUT        | Update an existing owner by ID             |
| /api/owners/<int:owner_id>          | DELETE     | Delete an existing owner by ID             |

### Cars

| Endpoint                            | HTTP Method | Result                                     |
| ----------------------------------- | -----------| ------------------------------------------ |
| /api/cars                           | GET        | Get all cars                                |
| /api/cars/<int:car_id>              | GET        | Get a single car by ID                      |
| /api/cars                           | POST       | Add a new car to an existing owner by ID    |
| /api/cars/<int:car_id>              | PUT        | Update an existing car by ID                |
| /api/cars/<int:car_id>              | DELETE     | Delete an existing car by ID                |



## 🚀 Author

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/74933799" width="100px;" alt="Foto do Kalel Leonardo Martinho no GitHub"/><br>
        <sub>
          <b>Kalel L. Martinho</b>
        </sub>
      </a>
      <p>
    Python Dev
      </p>
    </td>
  </tr>
</table>

## License

This project is licensed under the MIT License 