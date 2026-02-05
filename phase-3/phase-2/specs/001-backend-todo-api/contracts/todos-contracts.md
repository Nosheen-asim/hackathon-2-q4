# API Contracts: Todo Endpoints

**Feature**: Backend Todo API
**Date**: 2026-02-04

## Todo Endpoints (Protected - Requires Authentication)

### GET /todos

**Description**: Retrieve all todos for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Request:**
- Method: GET
- Endpoint: `/todos`
- Query Parameters (optional):
  - `completed`: boolean (filter by completion status)
  - `limit`: integer (number of results to return, default: 50, max: 100)
  - `offset`: integer (number of results to skip, default: 0)

**Response (Success - 200 OK):**
```json
{
  "todos": [
    {
      "id": "string",
      "title": "string",
      "description": "string or null",
      "completed": "boolean",
      "user_id": "string",
      "created_at": "string (ISO 8601 datetime)",
      "updated_at": "string (ISO 8601 datetime)"
    }
  ],
  "total_count": "integer",
  "limit": "integer",
  "offset": "integer"
}
```

---

### POST /todos

**Description**: Create a new todo for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Request:**
- Method: POST
- Endpoint: `/todos`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "title": "string (required, max 200 chars)",
    "description": "string or null (optional, max 1000 chars)",
    "completed": "boolean (optional, default: false)"
  }
  ```

**Response (Success - 201 Created):**
```json
{
  "id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "user_id": "string",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "detail": "string (validation error message)"
}
```

---

### GET /todos/{id}

**Description**: Retrieve a specific todo by ID for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Path Parameters:**
- `id`: string (required, todo ID)

**Request:**
- Method: GET
- Endpoint: `/todos/{id}`

**Response (Success - 200 OK):**
```json
{
  "id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "user_id": "string",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "detail": "string (todo not found or not owned by user)"
}
```

---

### PUT /todos/{id}

**Description**: Update an entire todo by ID for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Path Parameters:**
- `id`: string (required, todo ID)

**Request:**
- Method: PUT
- Endpoint: `/todos/{id}`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "title": "string (required, max 200 chars)",
    "description": "string or null (optional, max 1000 chars)",
    "completed": "boolean"
  }
  ```

**Response (Success - 200 OK):**
```json
{
  "id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "user_id": "string",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "detail": "string (todo not found or not owned by user)"
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "detail": "string (validation error message)"
}
```

---

### PATCH /todos/{id}

**Description**: Partially update a todo by ID for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Path Parameters:**
- `id`: string (required, todo ID)

**Request:**
- Method: PATCH
- Endpoint: `/todos/{id}`
- Content-Type: `application/json`
- Body (any combination of):
  ```json
  {
    "title": "string (optional, max 200 chars)",
    "description": "string or null (optional, max 1000 chars)",
    "completed": "boolean (optional)"
  }
  ```

**Response (Success - 200 OK):**
```json
{
  "id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "user_id": "string",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "detail": "string (todo not found or not owned by user)"
}
```

**Response (Error - 400 Bad Request):**
```json
{
  "detail": "string (validation error message)"
}
```

---

### PATCH /todos/{id}/complete

**Description**: Toggle the completion status of a todo by ID for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Path Parameters:**
- `id`: string (required, todo ID)

**Request:**
- Method: PATCH
- Endpoint: `/todos/{id}/complete`
- Content-Type: `application/json`
- Body:
  ```json
  {
    "completed": "boolean (required, new completion status)"
  }
  ```

**Response (Success - 200 OK):**
```json
{
  "id": "string",
  "title": "string",
  "description": "string or null",
  "completed": "boolean",
  "user_id": "string",
  "created_at": "string (ISO 8601 datetime)",
  "updated_at": "string (ISO 8601 datetime)"
}
```

**Response (Error - 404 Not Found):**
```json
{
  "detail": "string (todo not found or not owned by user)"
}
```

---

### DELETE /todos/{id}

**Description**: Delete a specific todo by ID for the authenticated user.

**Headers:**
- Authorization: `Bearer {access_token}`

**Path Parameters:**
- `id`: string (required, todo ID)

**Request:**
- Method: DELETE
- Endpoint: `/todos/{id}`

**Response (Success - 204 No Content):**
- Empty response body

**Response (Error - 404 Not Found):**
```json
{
  "detail": "string (todo not found or not owned by user)"
}
```

---

## Authentication Error Responses (for all protected endpoints)

**Response (Error - 401 Unauthorized):**
```json
{
  "detail": "string (not authenticated or invalid token)"
}
```