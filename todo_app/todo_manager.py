"""Todo Manager Class Definition."""

from typing import List, Optional
from .todo_item import TodoItem


class TodoManager:
    """
    Manages all todo items in memory.
    Handles add, view, update, delete, and complete/incomplete operations.
    """

    def __init__(self):
        """Initialize the todo manager with an empty list of todos."""
        self.todos: List[TodoItem] = []
        self._next_id = 1

    def add_todo(self, description: str) -> TodoItem:
        """
        Add a new todo item with the given description.

        Args:
            description: The description of the new todo

        Returns:
            The newly created TodoItem
        """
        if not description.strip():
            raise ValueError("Todo description cannot be empty")

        todo = TodoItem(id=self._next_id, description=description.strip())
        self.todos.append(todo)
        self._next_id += 1
        return todo

    def get_all_todos(self) -> List[TodoItem]:
        """
        Get all todo items.

        Returns:
            A list of all TodoItems
        """
        return self.todos.copy()

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """
        Get a todo item by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The TodoItem if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update a todo item's description.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description for the todo

        Returns:
            True if the todo was updated, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return False

        todo.update_description(new_description)
        return True

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_todo_complete(self, todo_id: int) -> bool:
        """
        Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was marked complete, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return False

        todo.mark_complete()
        return True

    def mark_todo_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo item as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            True if the todo was marked incomplete, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo is None:
            return False

        todo.mark_incomplete()
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new todo.

        Returns:
            The next available ID
        """
        return self._next_id