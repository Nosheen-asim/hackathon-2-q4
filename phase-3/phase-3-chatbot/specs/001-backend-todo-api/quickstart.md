# Quickstart Guide: Backend Todo API

**Feature**: Backend Todo API
**Date**: 2026-02-04

## Getting Started

This guide will help you set up, run, and test the Backend Todo API.

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Neon PostgreSQL account and database URL
- Better Auth secret key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn sqlmodel python-jose[cryptography] passlib[bcrypt] psycopg2-binary python-dotenv python-multipart
   ```

4. **Set up environment variables:**
   Copy the `.env.example` file to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your configuration:
   ```env
   NEON_DB_URL=your_neon_postgres_url
   AUTH_SECRET=your_better_auth_secret
   AUTH_URL=http://localhost:3000
   ```

### Running the Application

1. **Start the development server:**
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

2. **Access the API:**
   - API root: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - Alternative docs: http://localhost:8000/redoc

### Testing the API

#### 1. User Registration
Register a new user account:
```bash
curl -X POST "http://localhost:8000/auth/signup" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

#### 2. User Authentication
Log in to get an access token:
```bash
curl -X POST "http://localhost:8000/auth/signin" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "securepassword123"
  }'
```

#### 3. Create a Todo
Create a new todo (replace `{ACCESS_TOKEN}` with your actual token):
```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Authorization: Bearer {ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a todo application with FastAPI",
    "completed": false
  }'
```

#### 4. Get User's Todos
Retrieve all todos for the authenticated user:
```bash
curl -X GET "http://localhost:8000/todos" \
  -H "Authorization: Bearer {ACCESS_TOKEN}"
```

#### 5. Update a Todo
Update an existing todo:
```bash
curl -X PUT "http://localhost:8000/todos/{TODO_ID}" \
  -H "Authorization: Bearer {ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a todo application with FastAPI",
    "completed": true
  }'
```

#### 6. Toggle Todo Completion
Toggle the completion status of a todo:
```bash
curl -X PATCH "http://localhost:8000/todos/{TODO_ID}/complete" \
  -H "Authorization: Bearer {ACCESS_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{
    "completed": true
  }'
```

#### 7. Delete a Todo
Delete a todo:
```bash
curl -X DELETE "http://localhost:8000/todos/{TODO_ID}" \
  -H "Authorization: Bearer {ACCESS_TOKEN}"
```

### API Documentation

- Interactive API documentation is available at: http://localhost:8000/docs
- Alternative documentation at: http://localhost:8000/redoc
- All endpoints are documented with request/response examples

### Troubleshooting

1. **Database Connection Issues:**
   - Verify your NEON_DB_URL is correct in the .env file
   - Ensure your Neon PostgreSQL database is accessible
   - Check that the database credentials are valid

2. **Authentication Issues:**
   - Verify AUTH_SECRET matches between backend and frontend
   - Ensure the AUTH_URL is set correctly
   - Check that JWT tokens are being sent in requests properly

3. **CORS Issues:**
   - Verify the frontend URL is properly configured in CORS middleware
   - Ensure the frontend is sending requests to the correct backend URL

### Next Steps

1. Implement proper error handling for all endpoints
2. Add input validation for all request bodies
3. Set up automated tests
4. Configure production-ready logging
5. Deploy to your preferred hosting platform