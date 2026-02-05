# Todo Operations Contract

**Feature**: Console-Based Todo App
**Date**: 2026-01-08

## Operation Definitions

### Add Todo
- **Operation**: CREATE
- **Input**: Todo description (string)
- **Output**: Created TodoItem with assigned ID
- **Validation**: Description must not be empty
- **Error Conditions**: Empty description

### View Todos
- **Operation**: READ_ALL
- **Input**: None
- **Output**: List of all TodoItems
- **Validation**: None
- **Error Conditions**: None

### Update Todo
- **Operation**: UPDATE
- **Input**: Todo ID (integer), new description (string)
- **Output**: Updated TodoItem
- **Validation**: ID must exist, description must not be empty
- **Error Conditions**: Invalid ID, empty description

### Delete Todo
- **Operation**: DELETE
- **Input**: Todo ID (integer)
- **Output**: Success/Failure status
- **Validation**: ID must exist
- **Error Conditions**: Invalid ID

### Mark Complete
- **Operation**: UPDATE_STATUS
- **Input**: Todo ID (integer)
- **Output**: Updated TodoItem
- **Validation**: ID must exist
- **Error Conditions**: Invalid ID

### Mark Incomplete
- **Operation**: UPDATE_STATUS
- **Input**: Todo ID (integer)
- **Output**: Updated TodoItem
- **Validation**: ID must exist
- **Error Conditions**: Invalid ID