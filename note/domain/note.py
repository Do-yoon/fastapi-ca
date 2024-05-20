from dataclasses import dataclass
from datetime import datetime
from sqlalchemy.orm import relationship

@dataclass
class Tag:
    id: str
    name: str
    created_at: datetime
    updated_at: datetime

@dataclass
class Note:
    id: str
    user_id: str
    title: str
    content: str
    memo_date: str
    created_at: datetime
    updated_at: datetime
