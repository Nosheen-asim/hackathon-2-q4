# Todo API Backend

A secure, scalable backend API for a Todo application using FastAPI, SQLModel, and Neon PostgreSQL.

## Features

- User authentication with JWT tokens
- Full CRUD operations for todo items
- Proper authorization to ensure users can only access their own data
- RESTful API design with consistent JSON responses
- Input validation and error handling

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLModel with Neon PostgreSQL
- **Authentication**: JWT with bcrypt password hashing
- **Validation**: Pydantic

## Setup

1. Clone the repository
2. Navigate to the backend directory
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and fill in your values:
   ```bash
   cp .env.example .env
   ```
6. Update the `.env` file with your configuration

## Running the Application

Start the development server:
```bash
uvicorn src.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.

Interactive documentation will be available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- `POST /auth/signup` - Register a new user
- `POST /auth/signin` - Authenticate and get access token
- `GET /auth/me` - Get current user info

### Todos
- `GET /todos` - Get all todos for current user
- `POST /todos` - Create a new todo
- `GET /todos/{id}` - Get a specific todo
- `PUT /todos/{id}` - Update a todo
- `PATCH /todos/{id}` - Partially update a todo
- `PATCH /todos/{id}/complete` - Toggle completion status
- `DELETE /todos/{id}` - Delete a todo

## Environment Variables

- `NEON_DB_URL`: Your Neon PostgreSQL connection string
- `AUTH_SECRET`: Secret key for JWT token signing
- `AUTH_URL`: Frontend URL for CORS configuration

## Security

- Passwords are securely hashed using bcrypt
- JWT tokens for authentication with configurable expiration
- Proper authorization checks to ensure users can only access their own data
- Input validation using Pydantic models