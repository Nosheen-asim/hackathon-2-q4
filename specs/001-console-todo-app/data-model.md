# Data Model: Console-Based Todo Application

**Feature**: Console-Based Todo App
**Date**: 2026-01-08

## Entities

### Todo Item

Represents a single task with properties:

| Property | Type | Description | Validation |
|----------|------|-------------|------------|
| id | Integer | Unique identifier | Auto-generated, positive integer |
| description | String | Task description | Non-empty string |
| completed | Boolean | Completion status | True/False |
| created_at | DateTime | Creation timestamp | Auto-generated |

### Relationships

None - all todo items are independent of each other.

## State Transitions

- `incomplete` → `complete`: When user marks todo as complete
- `complete` → `incomplete`: When user marks todo as incomplete

## Validation Rules

- Description must not be empty
- ID must be unique within the application session
- ID must be a positive integer