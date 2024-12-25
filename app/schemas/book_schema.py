from pydantic import BaseModel
from typing import List, Optional

class UpdateBookSchema(BaseModel):
    ISBN: Optional[str] = None
    availability: Optional[str] = None
    brand: Optional[str] = None
    delivery: Optional[List[str]] = None
    description: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None
    rating: Optional[str] = None
    reviews_count: Optional[int] = None
    title: Optional[str] = None
    categories: Optional[str] = None
