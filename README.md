# Casting Agency
This website lets you store movies and actors in a database, and certain roles can make certain actions.

## Getting Started
This project is deployed over the domain:
https://casting-agency-314.herokuapp.com/
To make any request to this website, you have to specify an endpoint and have a role.

## Roles
There are three roles, all with different permessions, a user without a role can not do anything.
Roles:
1. Casting Assistant: Can only access movies and actors.
1. Casting Director: Can also edit movies and actors, and add or delete a new actor.
1. Executive Producer: Can also add or delete a new movie.

For of the three roles, I provide a working jwt token below, for testing purposes:
- Casting Assistant: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNkM2QzNDAyODUwMDcxNjAzNDIxIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTk1MjQsImV4cCI6MTYxMTg0NTkyNCwiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.SZrowdJAlDRZwNyOpDyIvnD74g4HrHJim60hj4A1IqaHw4didkBAZGxi3TCsM2v_6lK0dlSR1tv2gwkhx_O_AR65kt9dtnZyISa-6Qh_I0zuZobsP3B27u_mVd9BmuSTxJlZEgfgylHVIUQFwK74eUya9jV_6KL2SN0JzJ2pQ1jqx_MhEeJBiCYDdDlLaeQRg-46d-l1EIHqjVB4Prw-bdDzrUEJZuoNG8TxFE2pXo4NzfL_E8KigxQDd3ZpgYyEwG2x12MC-eKobgbdp0qkExOPE7oRT0nvksexPsQPqRJKCEHbyH-Uv5U38a-9TfDCZIqaM9VFXmXcneDKExYmkg

- Casting Director:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzNjYmVmZmNiZTIwMDZhODg1ZmRiIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTkzNzMsImV4cCI6MTYxMTg0NTc3MywiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.w0vuLmHVYeklBNMk4O1ZQHTO9V8sdnBr3_Rvh_HqJ1fNeJt6yh_svdSJ5CtpkQ8l5iWgJp5HR7SdLeatHtUjPDgm-mMBLjplbEE3lM3zLZLwrSUB597FsEf6KjUj1ZwU__YArTbeFxW5RUbYQCJGGkf_ZL-r-DuovAXC_V2HAWtg4T4z9iiPdtbGWYDPgE2XOdINTxTI6OZf7zpOoYVitf5gjon0B2ZyLLnOjTYPLYehunu65DI9jAgBRTBPA5fKYhSj8x5OpkneGNjuxnHJpLKudmGOSNUa8tNVP-pReEUwmmrGt3tjmdUMA2mRurEFBP2Mxm2iUfpzRYfRNrLc-w

- Executive Producer:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik9pazhMMHdaZGRQMll6OGhEQzhfRSJ9.eyJpc3MiOiJodHRwczovL21vYXBwcy51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwYzE5OWEzNDAyODUwMDcxNjAzMjdlIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE2MTE3NTkyNTcsImV4cCI6MTYxMTg0NTY1NywiYXpwIjoiTmlTaXoxb2kxQkNEcWVDbW5QOEpRemdSOXl1SmJJMWMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Nj---xU9kHTffIZF4IUG1FGbdE4nmPAXDnQDSETBkFwUjE00rSH2NrWTCdktyF02705b8Sr8R3vn3nKHdfTpI6yrw1MLg-9FILwK2ogbzaE-30vpfFmrUpaB0I2KmgmVTOvOaJL_5g2V9yoxwitaiFD__4Mk5Hmb_sEwo1IIYRe-q1ueN_9MC_zm5ouTLCsMlMUSWLJIvmq0tyUnGkl-UkFao6fQ1n-oHJ9PTXUwRBLJvkQjgkoq7LfgOkQXxYW_a2MOYoHUZ6pdTfRj8vFw8BQvn6DO46Nud_8Ov9cYsuvAuFYZ9M50hjj5YSRF_eZH9KqwOyplMxaP2JpCkMr9vQ

#### Endpoints
- GET /movies
    - Fetches all movies in the database
    - Request Arguments: None
    - Roles:
        - Casting Assistant
        - Casting Director
        - Executice Producer

###### Response
```
{
"success":true
"movies":[
  {
  "id",
  "title",
  "release_date"
  },
...
]
}
```

- GET /actors
    - Fetches all actors in the database
    - Request Arguments: None
    - Roles:
        - Casting Assistant
        - Casting Director
        - Executice Producer
###### Response
```
{
"success":true
"actors":[
  {
  "id",
  "name",
  "age",
  "gender"
  },
...
]
}
```

- POST /movies
    - Creates a new movie
    - Request Body:
        - title
        - release_date
    - Roles:
        - Executive Producer
    
###### Response
```
{
"success":true
"movie":
  {
  "id",
  "title",
  "release_date",
  }
}
```

- POST /actors
    - Creates a new actor
    - Request Body:
        - name
        - age
        - gender
    - Roles:
        - Casting Director
        - Executive Producer
    
###### Response
```
{
"success":true
"actor":
  {
  "id",
  "name",
  "age",
  "gender"
  }
}
```

- PATCH /movies/id
    - Modifies the movie with the given id
    - Request Body:
        - title
        - release_date
    - Roles:
        - Casting Director
        - Executive Producer
    
###### Response
```
{
"success":true
"movie":
  {
  "id",
  "title",
  "release_date",
  }
}
```

- PATCH /actors/id
    - Modifies the actor with the given id
    - Request Body:
        - name
        - age
        - gender
    - Roles:
        - Casting Director
        - Executive Producer
    
###### Response
```
{
"success":true
"movie":
  {
  "id",
  "name",
  "age",
  "gender"
  }
}
```

- DELETE /movies/id
    - Deletes the movie with the given id
    - Request Arguments: None
    - Roles:
        - Executive Producer
    
###### Response
```
{
"success":true
"movie":
  {
  "id",
  "title",
  "release_date",
  }
}
```

- DELETE /actors/id
    - Deletes the actor with the given id
    - Request Arguments: None
    - Roles:
        - Casting Director
        - Executive Producer
    
###### Response
```
{
"success":true
"actor":
  {
  "id",
  "name",
  "age",
  "gender"
  }
}
```






## Auhtors
- Mohammad Abdallah
