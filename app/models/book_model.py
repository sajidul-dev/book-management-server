from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class BookModel(BaseModel):
    isbn: List[str]
    author_name: List[str]
    title: str
    category: List[str]
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updatedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
