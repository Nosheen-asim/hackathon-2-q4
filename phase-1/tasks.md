---
description: "Task list template for feature implementation"
---

# Tasks: Console-Based Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 Create main.py entry point file
- [X] T003 [P] Create todo_app package directory and __init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create TodoItem class in todo_app/todo_item.py
- [X] T005 Create TodoManager class in todo_app/todo_manager.py
- [X] T006 Create CLI interface skeleton in todo_app/cli_interface.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new todo items to their list through the console interface

**Independent Test**: Can be fully tested by running the application, entering the add command, and verifying the todo appears in the list

### Implementation for User Story 1

- [X] T007 [P] [US1] Implement TodoItem model with required properties in todo_app/todo_item.py
- [X] T008 [P] [US1] Implement add_todo method in TodoManager class in todo_app/todo_manager.py
- [X] T009 [US1] Implement add todo functionality in CLI interface in todo_app/cli_interface.py
- [X] T010 [US1] Connect add todo functionality from CLI to manager in main.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo Items (Priority: P1)

**Goal**: Allow users to view all their current todo items through the console interface

**Independent Test**: Can be fully tested by running the application, adding some todos, and viewing the complete list

### Implementation for User Story 2

- [X] T011 [P] [US2] Implement get_all_todos method in TodoManager class in todo_app/todo_manager.py
- [X] T012 [US2] Implement view todos functionality in CLI interface in todo_app/cli_interface.py
- [X] T013 [US2] Connect view todos functionality from CLI to manager in main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Todo Item (Priority: P2)

**Goal**: Allow users to modify an existing todo item through the console interface

**Independent Test**: Can be fully tested by running the application, adding a todo, updating it, and verifying the changes

### Implementation for User Story 3

- [X] T014 [P] [US3] Implement update_todo method in TodoManager class in todo_app/todo_manager.py
- [X] T015 [US3] Implement update todo functionality in CLI interface in todo_app/cli_interface.py
- [X] T016 [US3] Connect update todo functionality from CLI to manager in main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Todo Item (Priority: P2)

**Goal**: Allow users to remove a todo item from their list through the console interface

**Independent Test**: Can be fully tested by running the application, adding todos, deleting one, and verifying it's removed from the list

### Implementation for User Story 4

- [X] T017 [P] [US4] Implement delete_todo method in TodoManager class in todo_app/todo_manager.py
- [X] T018 [US4] Implement delete todo functionality in CLI interface in todo_app/cli_interface.py
- [X] T019 [US4] Connect delete todo functionality from CLI to manager in main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Mark Todo as Complete (Priority: P3)

**Goal**: Allow users to mark a todo item as complete/incomplete through the console interface

**Independent Test**: Can be fully tested by running the application, adding a todo, marking it as complete, and verifying the status change

### Implementation for User Story 5

- [X] T020 [P] [US5] Implement mark_todo_complete and mark_todo_incomplete methods in TodoManager class in todo_app/todo_manager.py
- [X] T021 [US5] Implement mark todo functionality in CLI interface in todo_app/cli_interface.py
- [X] T022 [US5] Connect mark todo functionality from CLI to manager in main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T023 [P] Add input validation and error handling throughout CLI interface in todo_app/cli_interface.py
- [X] T024 [P] Add user-friendly menu display in CLI interface in todo_app/cli_interface.py
- [X] T025 Add proper error messages for invalid operations in todo_app/todo_manager.py
- [X] T026 [P] Create test script to verify all functionality in test_todo_app.py
- [X] T027 Run quickstart validation and update documentation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### Within Each User Story

- Models before services
- Services before UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Implementation Strategy

### MVP First (User Stories 1-2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Add Todo)
4. Complete Phase 4: User Story 2 (View Todos)
5. **STOP and VALIDATE**: Test User Stories 1-2 together
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Basic Add!)
3. Add User Story 2 → Test with Story 1 → Deploy/Demo (Add + View!)
4. Add User Story 3 → Test with others → Deploy/Demo (Add + View + Update!)
5. Add User Story 4 → Test with others → Deploy/Demo (Full CRUD!)
6. Add User Story 5 → Test with others → Deploy/Demo (Complete workflow!)
7. Each story adds value without breaking previous stories