from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class BookModel(BaseModel):
    ISBN: str
    availability: str
    brand: str
    delivery: List[str]
    description: Optional[str] = None
    price: float
    image_url: str
    rating: str
    reviews_count: int
    title: str
    categories: str
    createdAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updatedAt: Optional[datetime] = Field(default_factory=datetime.utcnow)
