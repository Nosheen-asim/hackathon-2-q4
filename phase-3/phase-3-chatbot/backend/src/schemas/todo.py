from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    title: str
    description: Optional[str] = None
    completed: bool = False

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI",
                "description": "Build a todo application with FastAPI",
                "completed": False
            }
        }


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Learn FastAPI",
                "completed": True
            }
        }


class TodoRead(TodoBase):
    id: str
    user_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TodoListResponse(BaseModel):
    todos: list[TodoRead]
    total_count: int
    limit: int
    offset: int


class TodoToggleComplete(BaseModel):
    completed: bool

    class Config:
        json_schema_extra = {
            "example": {
                "completed": True
            }
        }