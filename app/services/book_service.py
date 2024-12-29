from app.core.database import database,books_collection
from app.helpers.book_helper import book_helper
from bson.objectid import ObjectId
from datetime import datetime,timezone
from typing import Optional, List
from fastapi import  HTTPException

# Add book
def add_book(book_data: dict) -> dict:

  try:
    book_data["createdAt"] = datetime.now(timezone.utc)   
    book_data["updatedAt"] = datetime.now(timezone.utc)   
    book = books_collection.insert_one(book_data)
  except Exception as e:
    raise HTTPException(status_code=400, detail=Exception)
  return book_helper(books_collection.find_one({"_id": book.inserted_id}))

# Get all books
def get_books(
    search: Optional[str],
    category: Optional[str],
    min_price: Optional[float],
    max_price: Optional[float],
    sort_by: Optional[str],
    sort_order: int,
    page: int,
    page_size: int,
) -> list:
    query = {}

    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"author_name": {"$regex": search, "$options": "i"}},
        ]

    if category:
        query["category"] = category

    if min_price is not None:
        query["price"] = {"$gte": min_price}
    if max_price is not None:
        query["price"] = {**query.get("price", {}), "$lte": max_price}

    skip = (page - 1) * page_size
    limit = page_size

    sort_criteria = [(sort_by, sort_order)] if sort_by else None

    total = books_collection.count_documents(query)
    books_cursor = books_collection.find(query,projection={"_id":True,"title": True, "author_name": True, "isbn": True, "category":True}).skip(skip).limit(limit)
    if sort_criteria:
        books_cursor = books_cursor.sort(sort_criteria)
    books = [book_helper(book) for book in books_cursor]

    return {
        "meta": {
            "page": page,
            "limit": page_size,
            "total": total,
        },
        "data": books,
    }

# Get single book
def get_book(book_id: str) -> dict:
  book = books_collection.find_one({"_id": ObjectId(book_id)})
  return book_helper(book) if book else None

# Update book
def update_book(book_id: str, book_data: dict) -> bool:
  book_data["updatedAt"] = datetime.now(timezone.utc)
  update_result = books_collection.update_one(
      {"_id": ObjectId(book_id)}, {"$set": book_data}
  )
  return update_result.modified_count > 0

# Delete book
def delete_book(book_id: str) -> bool:
    delete_result = books_collection.delete_one({"_id": ObjectId(book_id)})
    return delete_result.deleted_count > 0

def get_categories() -> List[str]:
    categories = books_collection.distinct("category")
    return categories
