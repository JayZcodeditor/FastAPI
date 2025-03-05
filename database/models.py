from pydantic import BaseModel
from datetime import datetime

class Todo(BaseModel):
    title: str
    description: str
    is_completed: bool = False
    is_deleted: bool = False
    update_At: int = int(datetime.timestamp(datetime.now()))
    creation: int = int(datetime.timestamp(datetime.now()))
