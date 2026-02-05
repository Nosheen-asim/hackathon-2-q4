# API Contracts: Authentication Endpoints

**Feature**: Backend Todo API
**Date**: 2026-02-04

## Authentication Endpoints

### POST /auth/signup

**Description**: Register a new user account with email and password.

**Request:**
- Method: POST
- Endpoint: `/auth/signup`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "email": "string (required, valid email format)",
    "password": "string (required, min 6 characters)"
  }
  ```

**Response (Success - 201 Created):**
```json
{
  "user": {
    "id": "string",
    "email": "string"
  },
  "access_token": "string",
  "token_type": "string (e.g., 'bearer')"
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "detail": "string (validation error message)"
}
```

**Response (Error - 409 Conflict):**
```json
{
  "detail": "string (email already registered)"
}
```

---

### POST /auth/signin

**Description**: Authenticate existing user with email and password.

**Request:**
- Method: POST
- Endpoint: `/auth/signin`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "email": "string (required, valid email format)",
    "password": "string (required)"
  }
  ```

**Response (Success - 200 OK):**
```json
{
  "user": {
    "id": "string",
    "email": "string"
  },
  "access_token": "string",
  "token_type": "string (e.g., 'bearer')"
}
```

**Response (Error - 401 Unauthorized):**
```json
{
  "detail": "string (invalid credentials)"
}
```

**Response (Error - 422 Unprocessable Entity):**
```json
{
  "detail": "string (validation error message)"
}
```