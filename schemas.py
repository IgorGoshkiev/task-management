from pydantic import BaseModel, validator
from datetime import datetime


class TaskCreate(BaseModel):
    title: str
    description: str
    deadline: str  # DD-MM-YYYY format

    @validator('deadline')
    def validate_deadline(cls, v):
        try:
            datetime.strptime(v, '%d-%m-%Y')
        except ValueError:
            raise ValueError('Deadline must be in DD-MM-YYYY format')
        return v


class TaskResponse(BaseModel):
    id: str
    title: str
    description: str
    deadline: str
    created_at: datetime
