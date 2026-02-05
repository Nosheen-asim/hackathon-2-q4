# Research & Decisions: Backend Todo API

**Feature**: Backend Todo API
**Date**: 2026-02-04

## Authentication Approach

### Decision: JWT-based Authentication with FastAPI Security Dependencies
We will implement JWT (JSON Web Tokens) for user authentication, using FastAPI's security dependencies for route protection.

### Rationale:
- JWT tokens are stateless and scale well with microservices
- FastAPI provides excellent built-in support for OAuth2 with JWT
- Secure token handling with proper expiration
- Compatible with Next.js frontend integration
- Standard industry practice for API authentication

### Alternatives considered:
- Session-based authentication: Would require server-side session storage and doesn't scale as well
- API Keys: Less secure for user authentication, better for service-to-service communication
- OAuth providers only: Doesn't meet requirement for direct email/password registration

## Database Technology Choice

### Decision: SQLModel with Neon PostgreSQL
We will use SQLModel as the ORM/ODM layer with Neon PostgreSQL as the database backend.

### Rationale:
- SQLModel combines the power of SQLAlchemy and Pydantic, providing type safety
- Neon offers serverless PostgreSQL with auto-scaling and global distribution
- Strong consistency and ACID compliance for user data integrity
- Excellent Python ecosystem support
- Supports complex queries needed for todo filtering and management

### Alternatives considered:
- MongoDB with PyMongo: Would lose relational integrity benefits
- SQLite: Not suitable for production-scale applications
- Supabase: While good, Neon PostgreSQL gives us more direct control

## Password Security

### Decision: bcrypt with passlib for password hashing
We will use bcrypt algorithm via the passlib library for secure password hashing.

### Rationale:
- bcrypt is the gold standard for password hashing
- passlib provides easy integration with proper salt generation
- Resistant to rainbow table attacks
- Adjustable cost factor for future security needs
- Industry standard for password security

### Alternatives considered:
- SHA-256 with salt: Vulnerable to brute force attacks
- Argon2: More modern but bcrypt is more widely adopted and proven
- Plain text: Never acceptable for production

## API Architecture

### Decision: RESTful API with FastAPI
We will implement a RESTful API architecture using FastAPI framework.

### Rationale:
- FastAPI provides automatic API documentation (Swagger/OpenAPI)
- Built-in request validation with Pydantic
- High performance comparable to Node.js/Go frameworks
- Excellent async support for handling concurrent requests
- Strong type hints and IDE support

### Alternatives considered:
- GraphQL: More complex for simple todo application
- Flask: Less performant and lacks automatic validation features
- Django REST Framework: Heavier framework than needed for this use case

## CORS Configuration

### Decision: Restrictive CORS policy allowing only frontend origin
We will implement CORS middleware allowing only the Next.js frontend origin.

### Rationale:
- Prevents unauthorized cross-origin requests
- Security best practice to limit origins
- Meets requirement to enable CORS for localhost:3000
- Reduces attack surface from malicious origins

### Alternatives considered:
- Wildcard CORS (*): Major security vulnerability
- Multiple origins: Unnecessary complexity for single frontend application

## Error Handling Strategy

### Decision: Consistent JSON error responses with appropriate HTTP status codes
We will implement centralized exception handling returning consistent JSON error formats.

### Rationale:
- Provides predictable error responses for frontend consumption
- Follows REST API best practices with proper HTTP status codes
- Enables better error handling in the Next.js frontend
- Improves debugging and monitoring capabilities

### Alternatives considered:
- Raw Python exceptions: Not suitable for API responses
- Custom error formats: Would complicate frontend error handling