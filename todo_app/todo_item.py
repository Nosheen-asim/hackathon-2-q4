"""Todo Item Class Definition."""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single todo item with properties:
    - id: Unique identifier for the todo
    - description: Text description of the todo
    - completed: Boolean indicating if the todo is completed
    - created_at: Timestamp when the todo was created
    """

    id: int
    description: str
    completed: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at timestamp if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

    def __str__(self) -> str:
        """Return a string representation of the todo item."""
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.description}"

    def mark_complete(self):
        """Mark the todo item as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the todo item as incomplete."""
        self.completed = False

    def update_description(self, new_description: str):
        """Update the todo item's description."""
        if not new_description.strip():
            raise ValueError("Description cannot be empty")
        self.description = new_description