from pydantic import BaseModel
from typing import List, Optional

class UpdateBookSchema(BaseModel):
    isbn: Optional[List[str]] = None
    author_name: Optional[List[str]] = None
    title: Optional[str] = None
    category: Optional[List[str]] = None

