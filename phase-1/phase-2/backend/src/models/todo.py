from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from .user import User


class TodoBase(SQLModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    user_id: str


class Todo(TodoBase, table=True):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str = Field(nullable=False, max_length=200)
    description: Optional[str] = Field(max_length=1000)
    completed: bool = False
    user_id: str = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user
    user: User = Relationship(back_populates="todos")


class TodoCreate(TodoBase):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TodoRead(TodoBase):
    id: str
    created_at: datetime
    updated_at: datetime