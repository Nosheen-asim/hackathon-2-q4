# Data Model: Backend Todo API

**Feature**: Backend Todo API
**Date**: 2026-02-04

## Entities

### User
Represents a registered user account in the system.

**Fields:**
- `id` (UUID/string): Unique identifier for the user (Primary Key)
- `email` (string): User's email address (unique, indexed)
- `hashed_password` (string): Securely hashed password using bcrypt
- `created_at` (datetime): Timestamp when the account was created (indexed)
- `updated_at` (datetime): Timestamp when the account was last updated

**Constraints:**
- Email must be unique across all users
- Email must follow standard email format validation
- Password must be securely hashed before storage
- Created timestamp set automatically on creation

**Relationships:**
- One-to-many relationship with Todo entities (one user owns many todos)

### Todo
Represents a task item owned by a specific user.

**Fields:**
- `id` (UUID/string): Unique identifier for the todo (Primary Key)
- `title` (string): Title or subject of the todo item (indexed)
- `description` (string, optional): Detailed description of the todo
- `completed` (boolean): Status indicating if the todo is completed (indexed)
- `user_id` (UUID/string): Foreign key linking to the owning user (indexed)
- `created_at` (datetime): Timestamp when the todo was created (indexed)
- `updated_at` (datetime): Timestamp when the todo was last updated

**Constraints:**
- Title is required and must not be empty
- Title has maximum length validation
- Description has optional maximum length validation
- Completed status defaults to false
- Associated user must exist (foreign key constraint)

**Relationships:**
- Many-to-one relationship with User entity (many todos belong to one user)

## Indexing Strategy

### Primary Indexes
- User.id: Primary key index
- Todo.id: Primary key index

### Secondary Indexes
- User.email: Unique index for fast authentication lookups
- User.created_at: Index for temporal queries
- Todo.user_id: Index for efficient user-specific todo retrieval
- Todo.completed: Index for filtering completed/incomplete todos
- Todo.created_at: Index for chronological ordering
- Todo.title: Index for search capabilities

## Validation Rules

### User Validation
- Email format: Must match standard email regex pattern
- Email uniqueness: No duplicate email addresses allowed
- Password strength: Minimum length and complexity requirements (handled during hashing)

### Todo Validation
- Title: Required, non-empty, maximum length of 200 characters
- Description: Optional, maximum length of 1000 characters
- User ownership: Todos can only be accessed/modified by their owner
- Completed status: Boolean value only (true/false)

## State Transitions

### Todo Completion States
- `incomplete` → `completed`: When user marks todo as done
- `completed` → `incomplete`: When user unmarks completed todo

## Access Control Rules

### Ownership Validation
- Users can only create todos associated with their own account
- Users can only read, update, or delete their own todos
- Admin users (if implemented later) may have additional privileges
- Cross-user data access is prohibited without explicit authorization