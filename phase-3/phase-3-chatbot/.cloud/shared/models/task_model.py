"""
Shared Task Model

Defines the common structure for tasks across all agents
"""

class TaskModel:
    def __init__(self, task_id=None, title="", description="", completed=False, user_id=None, created_at=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.user_id = user_id
        self.created_at = created_at

    def to_dict(self):
        """Convert the task object to a dictionary representation"""
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "user_id": self.user_id,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a TaskModel instance from a dictionary"""
        return cls(
            task_id=data.get('task_id'),
            title=data.get('title', ''),
            description=data.get('description', ''),
            completed=data.get('completed', False),
            user_id=data.get('user_id'),
            created_at=data.get('created_at')
        )