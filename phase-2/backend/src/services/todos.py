from sqlmodel import Session, select
from typing import List, Optional
from ..models.todo import Todo, TodoCreate, TodoUpdate
from ..models.user import User


def create_todo(session: Session, todo_create: TodoCreate, user_id: str) -> Todo:
    """Create a new todo for a user"""
    db_todo = Todo(
        title=todo_create.title,
        description=todo_create.description,
        completed=todo_create.completed,
        user_id=user_id
    )

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo


def get_todos_by_user(
    session: Session,
    user_id: str,
    completed: Optional[bool] = None,
    limit: int = 50,
    offset: int = 0
) -> tuple[List[Todo], int]:
    """Get todos for a specific user with optional filters"""
    query = select(Todo).where(Todo.user_id == user_id)

    if completed is not None:
        query = query.where(Todo.completed == completed)

    # Get total count
    count_query = select(Todo).where(Todo.user_id == user_id)
    if completed is not None:
        count_query = count_query.where(Todo.completed == completed)

    total_count = len(session.exec(count_query).all())

    # Apply limit and offset
    query = query.offset(offset).limit(limit)

    todos = session.exec(query).all()

    return todos, total_count


def get_todo_by_id_and_user(session: Session, todo_id: str, user_id: str) -> Optional[Todo]:
    """Get a specific todo by ID for a specific user"""
    todo = session.get(Todo, todo_id)
    if todo and todo.user_id == user_id:
        return todo
    return None


def update_todo(session: Session, todo_id: str, todo_update: TodoUpdate, user_id: str) -> Optional[Todo]:
    """Update a todo by ID for a specific user"""
    todo = get_todo_by_id_and_user(session, todo_id, user_id)
    if not todo:
        return None

    # Update fields that are provided
    update_data = todo_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)

    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


def toggle_todo_completion(session: Session, todo_id: str, completed: bool, user_id: str) -> Optional[Todo]:
    """Toggle the completion status of a todo"""
    todo = get_todo_by_id_and_user(session, todo_id, user_id)
    if not todo:
        return None

    todo.completed = completed
    session.add(todo)
    session.commit()
    session.refresh(todo)

    return todo


def delete_todo(session: Session, todo_id: str, user_id: str) -> bool:
    """Delete a todo by ID for a specific user"""
    todo = get_todo_by_id_and_user(session, todo_id, user_id)
    if not todo:
        return False

    session.delete(todo)
    session.commit()

    return True