"""
Shared Conversation Model

Defines the common structure for conversations across all agents
"""

class ConversationModel:
    def __init__(self, conversation_id=None, user_id=None, created_at=None, updated_at=None):
        self.conversation_id = conversation_id
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        """Convert the conversation object to a dictionary representation"""
        return {
            "conversation_id": self.conversation_id,
            "user_id": self.user_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        """Create a ConversationModel instance from a dictionary"""
        return cls(
            conversation_id=data.get('conversation_id'),
            user_id=data.get('user_id'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )