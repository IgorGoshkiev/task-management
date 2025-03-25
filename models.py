from datetime import datetime
from uuid import uuid4
from typing import Dict


class Task:
    def __init__(self, title: str, description: str, deadline: str):
        self.id = str(uuid4())
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now()

    def dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "deadline": self.deadline,
            "created_at": self.created_at
        }


# In-memory storage
tasks: Dict[str, Task] = {}
