from fastapi import APIRouter, HTTPException, Query, HTTPException
from app.models.book_model import BookModel
from app.schemas.book_schema import UpdateBookSchema
from app.services.book_service import add_book, get_books, get_book, update_book, delete_book, get_categories
from typing import Optional
import requests
from app.core.database import books_collection


router = APIRouter()

@router.post("/books")
def create_book(book: BookModel):
  return add_book(book.dict())

@router.get("/books")
def read_books(
    search: Optional[str] = Query(None, description="Search by title or brand"),
    category: Optional[str] = Query(None, description="Filter by category"),
    min_price: Optional[float] = Query(None, description="Minimum price"),
    max_price: Optional[float] = Query(None, description="Maximum price"),
    sort_by: Optional[str] = Query(None, description="Field to sort by (e.g., price, reviews_count)"),
    sort_order: Optional[int] = Query(1, description="Sort order: 1 for ascending, -1 for descending"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Number of items per page"),
):
    page = int(page)
    page_size = int(page_size)
    
    return get_books(
        search=search,
        category=category,
        min_price=min_price,
        max_price=max_price,
        sort_by=sort_by,
        sort_order=sort_order,
        page=page,
        page_size=page_size,
    )

@router.get("/books/{book_id}")
def read_book(book_id: str):
  book = get_book(book_id)
  if not book:
      raise HTTPException(status_code=404, detail="Book not found")
  return book

@router.put("/book/{book_id}")
def modify_book(book_id: str, book: UpdateBookSchema):
  if not update_book(book_id, book.dict(exclude_unset=True)):
      raise HTTPException(status_code=404, detail="Book not found or no changes made")
  return {"message": "Book updated successfully"}

@router.delete("/books/{book_id}")
def remove_book(book_id: str):
    if not delete_book(book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}

@router.get("/categories")
def get_all_categories():
    categories = get_categories()
    return {"categories": categories}

@router.post("/retrieve-books")
def retrieve_books():
    url="https://openlibrary.org/search.json?q=the+lord+of+the+rings"
    response = requests.get(url)
    data = response.json()
    books = []
    for doc in data.get("docs", []):
        book = {
            "title": doc.get("title"),
            "isbn": doc.get("isbn"),
            "author_name": doc.get("author_name"),
            "category": doc.get("subject",[]),
        }
        saved_book=add_book(book)
        books.append(saved_book)
    
    return {"books": data}
    
@router.put("/update-brand-to-author")
def update_brand_to_author():
    try:
        
        result = books_collection.update_many(
            {"ISBN": {"$exists": True}},  
            [
                {
                    "$set": {
                        "isbn": {
                            "$cond": {
                                "if": {"$isArray": "$ISBN"},
                                "then": "$ISBN",
                                "else": ["$ISBN"],
                            }
                        }
                    }
                },
                {"$unset": "ISBN"},  
            ],
        )

        return {
            "message": "Update operation completed",
            "matched_count": result.matched_count,
            "modified_count": result.modified_count,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))