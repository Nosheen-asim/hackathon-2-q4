from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from typing import List, Optional
from ..schemas.todo import TodoCreate, TodoUpdate, TodoRead, TodoListResponse, TodoToggleComplete
from ..services.todos import (
    create_todo, get_todos_by_user, get_todo_by_id_and_user,
    update_todo, toggle_todo_completion, delete_todo
)
from ..config.database import get_session
from ..utils.auth import get_current_active_user
from ..models.user import User


router = APIRouter()


@router.get("/", response_model=TodoListResponse)
def read_todos(
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session),
    completed: Optional[bool] = Query(None, description="Filter by completion status"),
    limit: int = Query(50, ge=1, le=100, description="Number of results to return"),
    offset: int = Query(0, ge=0, description="Number of results to skip")
):
    """Get all todos for the current user"""
    todos, total_count = get_todos_by_user(
        session, current_user.id, completed=completed, limit=limit, offset=offset
    )

    return TodoListResponse(
        todos=todos,
        total_count=total_count,
        limit=limit,
        offset=offset
    )


@router.post("/", response_model=TodoRead, status_code=status.HTTP_201_CREATED)
def create_new_todo(
    todo_create: TodoCreate,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Create a new todo for the current user"""
    # Ensure the user_id in the request matches the authenticated user
    todo_create_dict = todo_create.model_dump()
    todo_create_dict['user_id'] = current_user.id

    from ..models.todo import TodoCreate as TodoCreateModel
    todo_to_create = TodoCreateModel(**todo_create_dict)

    return create_todo(session, todo_to_create, current_user.id)


@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(
    todo_id: str,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Get a specific todo by ID"""
    todo = get_todo_by_id_and_user(session, todo_id, current_user.id)
    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or not owned by user"
        )
    return todo


@router.put("/{todo_id}", response_model=TodoRead)
def update_existing_todo(
    todo_id: str,
    todo_update: TodoUpdate,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Update an entire todo by ID"""
    updated_todo = update_todo(session, todo_id, todo_update, current_user.id)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or not owned by user"
        )
    return updated_todo


@router.patch("/{todo_id}", response_model=TodoRead)
def partial_update_todo(
    todo_id: str,
    todo_update: TodoUpdate,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Partially update a todo by ID"""
    updated_todo = update_todo(session, todo_id, todo_update, current_user.id)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or not owned by user"
        )
    return updated_todo


@router.patch("/{todo_id}/complete", response_model=TodoRead)
def toggle_todo_complete(
    todo_id: str,
    toggle_data: TodoToggleComplete,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Toggle the completion status of a todo"""
    updated_todo = toggle_todo_completion(session, todo_id, toggle_data.completed, current_user.id)
    if not updated_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or not owned by user"
        )
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_todo(
    todo_id: str,
    current_user: User = Depends(get_current_active_user),
    session: Session = Depends(get_session)
):
    """Delete a specific todo by ID"""
    success = delete_todo(session, todo_id, current_user.id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found or not owned by user"
        )
    return