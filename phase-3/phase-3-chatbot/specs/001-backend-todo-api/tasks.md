---
description: "Task list for Backend Todo API implementation"
---

# Tasks: Backend Todo API

**Input**: Design documents from `/specs/[001-backend-todo-api]/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only if tests requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Backend**: `backend/src/` at project root
- Paths shown below follow the planned structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend directory structure per implementation plan
- [x] T002 Initialize Python virtual environment
- [x] T003 [P] Install dependencies (fastapi, uvicorn, sqlmodel, psycopg2, passlib, python-jose, python-dotenv)
- [x] T004 Create requirements.txt and requirements-dev.txt
- [x] T005 Create .env.example file with required environment variables
- [x] T006 Create main.py entry point in backend/src/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 [P] Create database configuration in backend/src/config/database.py
- [x] T008 [P] Create settings configuration in backend/src/config/settings.py
- [x] T009 [P] Create security utilities in backend/src/utils/security.py
- [x] T010 [P] Create authentication utilities in backend/src/utils/auth.py
- [x] T011 [P] Create JWT token utilities in backend/src/utils/auth.py
- [x] T012 [P] Create password hashing utilities in backend/src/utils/security.py
- [x] T013 Configure CORS middleware for frontend integration in backend/src/main.py
- [x] T014 [P] Create exception handlers in backend/src/main.py
- [x] T015 Set up database engine and session in backend/src/config/database.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure User Registration and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable users to register for an account and securely authenticate themselves so that they can access their personal todo list.

**Independent Test**: New users can register with email and password, then successfully log in to receive a valid authentication token, demonstrating the core security mechanism works.

### Implementation for User Story 1

- [x] T016 [P] [US1] Create User model in backend/src/models/user.py
- [x] T017 [P] [US1] Create User schemas in backend/src/schemas/user.py
- [x] T018 [P] [US1] Create auth service in backend/src/services/auth.py
- [x] T019 [US1] Create auth routes in backend/src/routes/auth.py
- [x] T020 [US1] Implement signup endpoint POST /auth/signup
- [x] T021 [US1] Implement signin endpoint POST /auth/signin
- [x] T022 [US1] Add password validation and hashing to auth endpoints
- [x] T023 [US1] Add JWT token creation and validation to auth flow
- [x] T024 [US1] Add proper error handling and validation responses

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Personal Todo Management (Priority: P2)

**Goal**: Allow authenticated users to create, read, update, and delete their personal todos so that they can manage their tasks effectively.

**Independent Test**: Authenticated users can perform all CRUD operations on their own todos independently of other users.

### Implementation for User Story 2

- [x] T025 [P] [US2] Create Todo model in backend/src/models/todo.py
- [x] T026 [P] [US2] Create Todo schemas in backend/src/schemas/todo.py
- [x] T027 [P] [US2] Create todos service in backend/src/services/todos.py
- [x] T028 [US2] Create todos routes in backend/src/routes/todos.py
- [x] T029 [US2] Implement GET /todos endpoint to retrieve user's todos
- [x] T030 [US2] Implement POST /todos endpoint to create new todos
- [x] T031 [US2] Implement GET /todos/{id} endpoint to retrieve specific todo
- [x] T032 [US2] Implement PUT /todos/{id} endpoint to update entire todo
- [x] T033 [US2] Implement DELETE /todos/{id} endpoint to delete todo
- [x] T034 [US2] Add user ownership validation to all todo endpoints
- [x] T035 [US2] Add proper error handling for unauthorized access

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Todo Completion Tracking (Priority: P3)

**Goal**: Allow authenticated users to mark their todos as completed or incomplete so that they can track their progress.

**Independent Test**: Authenticated users can toggle the completion status of their todos and see the updated status reflected in their list.

### Implementation for User Story 3

- [x] T036 [US3] Implement PATCH /todos/{id}/complete endpoint to toggle completion status
- [x] T037 [P] [US3] Add PATCH /todos/{id} endpoint for partial updates
- [x] T038 [US3] Add query parameters support to GET /todos (completed, limit, offset)
- [x] T039 [US3] Add response pagination to GET /todos endpoint
- [x] T040 [US3] Add proper validation to completion toggle endpoint

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Security & Middleware (Priority: P4)

**Goal**: Add authentication middleware and security measures to protect all endpoints.

**Independent Test**: All protected endpoints require valid authentication tokens and reject unauthorized requests.

### Implementation for Security & Middleware

- [x] T041 [P] Create authentication middleware in backend/src/middleware/auth_middleware.py
- [x] T042 [P] Create authentication dependency in backend/src/utils/auth.py
- [x] T043 [US2] Apply authentication dependency to all todos endpoints
- [x] T044 [US3] Apply authentication dependency to completion toggle endpoint
- [x] T045 Add proper authorization checks to ensure users can only access their own data
- [x] T046 Add rate limiting concept (middleware preparation)
- [x] T047 Add input sanitization to all request handlers

**Checkpoint**: All endpoints now have proper authentication and authorization

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T048 [P] Add comprehensive error handling across all endpoints
- [x] T049 [P] Add logging configuration for audit trails
- [x] T050 [P] Add input validation to all request schemas
- [x] T051 [P] Add database transaction handling where needed
- [x] T052 Add automated tests (unit/integration) for all endpoints
- [x] T053 Add API documentation and examples
- [x] T054 [P] Add environment-specific configurations
- [x] T055 Run integration testing to validate complete flow
- [x] T056 Final security review and hardening

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Security (Phase 6)**: Depends on User Stories 2 and 3 completion
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on User Story 1 (auth)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Depends on User Story 2 (todos)
- **Security (P4)**: Depends on User Stories 2 and 3 completion

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 2

```bash
# Launch all components for User Story 2 together:
Task: "Create Todo model in backend/src/models/todo.py"
Task: "Create Todo schemas in backend/src/schemas/todo.py"
Task: "Create todos service in backend/src/services/todos.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add Security → Test independently → Deploy/Demo
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2 (waits for auth from US1)
   - Developer C: User Story 3 (waits for todos from US2)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence