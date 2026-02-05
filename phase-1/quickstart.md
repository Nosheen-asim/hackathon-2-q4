# Quickstart: Console-Based Todo Application

**Feature**: Console-Based Todo App
**Date**: 2026-01-08

## Getting Started

1. Clone the repository
2. Navigate to the project directory
3. Run the application with: `python main.py`
4. Follow the menu prompts to interact with the todo application

## Available Commands

1. **Add a new todo**: Creates a new todo item with the provided description
2. **View all todos**: Displays all todos with their completion status
3. **Update a todo**: Modifies the description of an existing todo
4. **Delete a todo**: Removes a todo from the list (with confirmation)
5. **Mark todo as complete**: Sets the completion status to true
6. **Mark todo as incomplete**: Sets the completion status to false
7. **Exit**: Closes the application (all data is lost)

## Example Usage

```
Welcome to the Todo Application!
This is a simple in-memory todo application.
All data will be lost when the application exits.

==================================================
           TODO APPLICATION
==================================================
1. Add a new todo
2. View all todos
3. Update a todo
4. Delete a todo
5. Mark todo as complete
6. Mark todo as incomplete
7. Exit
==================================================
Enter your choice (1-7):
```

## Notes

- All data is stored in memory only and will be lost when the application exits
- Each todo receives a unique ID automatically
- The application validates all user inputs and provides appropriate error messages