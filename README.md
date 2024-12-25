# Book Management API

## Overview

This application is a **Book Management API** built using **FastAPI** and **MongoDB**, following a modular design pattern for scalability and maintainability. It provides the following features:

- Add a new book
- Retrieve all books
- Retrieve a single book by ID
- Update a book by ID
- Delete a book by ID

---

## Project Structure

```
book_management/
│
├── app/
│   ├── main.py                 # Entry point for the application
│   ├── core/
│   │   ├── config.py           # Configuration settings (e.g., database URI)
│   │   └── database.py         # MongoDB connection
│   ├── models/
│   │   └── book.py             # Pydantic models
│   ├── routes/
│   │   └── book_routes.py      # Routes for book operations
│   └── services/
│       └── book_service.py     # Business logic for book operations
│
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## Installation

### Prerequisites

- Python 3.8+
- MongoDB installed and running

### Steps

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd book_management
   ```

2. Create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up MongoDB:

   - Ensure MongoDB is running locally or update the `MONGODB_URI` in `app/core/config.py` to point to your MongoDB instance.

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## API Endpoints

### Base URL

`http://127.0.0.1:8000`

### Endpoints

| Method | Endpoint               | Description            |
| ------ | ---------------------- | ---------------------- |
| POST   | `/api/books`           | Add a new book         |
| GET    | `/api/books`           | Retrieve all books     |
| GET    | `/api/books/{book_id}` | Retrieve a single book |
| PUT    | `/api/books/{book_id}` | Update a book by ID    |
| DELETE | `/api/books/{book_id}` | Delete a book by ID    |

---

## Example Usage

### Adding a Book

**Request**:

```json
POST /api/books
{
  "title": "The Great Gatsby",
  "ISBN":"3485832",
  "author": "F. Scott Fitzgerald",
  "description": "A novel set in the Jazz Age",
  "year": 1925
}
```

**Response**:

```json
{
  "id": "60b8d295f4d2b9a2f828c2b1",
  "title": "The Great Gatsby",
  "ISBN": "3485832",
  "author": "F. Scott Fitzgerald",
  "description": "A novel set in the Jazz Age",
  "year": 1925
}
```

### Getting All Books

**Request**:

```http
GET /api/books
```

**Response**:

```json
[
  {
    "id": "60b8d295f4d2b9a2f828c2b1",
    "title": "The Great Gatsby",
    "ISBN": "3485832",
    "author": "F. Scott Fitzgerald",
    "description": "A novel set in the Jazz Age",
    "year": 1925
  }
]
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
