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
| PUT    | `/api/book/{book_id}` | Update a book by ID    |
| DELETE | `/api/books/{book_id}` | Delete a book by ID    |

---

## Example Usage

### Adding a Book

**Request**:

```json
POST /api/books
{
  "ISBN": "string",
  "availability": "string",
  "brand": "string",
  "delivery": [
    "string"
  ],
  "description": "string",
  "price": 0,
  "image_url": "string",
  "rating": "string",
  "reviews_count": 0,
  "title": "string",
  "categories": "string"
}
```

**Response**:

```json
{
  "ISBN": "string",
  "availability": "string",
  "brand": "string",
  "delivery": [
    "string"
  ],
  "description": "string",
  "price": 0,
  "image_url": "string",
  "rating": "string",
  "reviews_count": 0,
  "title": "string",
  "categories": "string"
}
```

### Getting All Books

**Request**:

```http
GET /api/books
```

**Response**:

```json
{
  "meta": {
    "page": 1,
    "limit": 10,
    "total": 1
  },
  "data": [
    {
      "_id": "67694574fa8bec94aab09a37",
      "ISBN": "9780007513765",
      "availability": "In Stock.",
      "brand": "Drew Daywalt",
      "delivery": [
        "FREE delivery Tuesday, December 28 if you spend $25 on items shipped by Amazon",
        "Arrives after Christmas. Need a gift sooner? Send an Amazon Gift Card instantly by email or SMS.",
        "FREE delivery Wednesday, December 29 if you spend $25 on items shipped by Amazon",
        "Arrives after Christmas. Need a gift sooner? Send an Amazon Gift Card instantly by email or SMS."
      ],
      "description": "Fiction book for children",
      "price": 12.08,
      "image_url": "https://images-na.ssl-images-amazon.com/images/I/51q21jP9MtL._SX218_BO1,204,203,200_QL40_ML2_.jpg",
      "rating": "4.8 out of 5 stars",
      "reviews_count": 16628,
      "title": "THE DAYS THE CRAYONS QUIT",
      "categories": "Children's Books",
      "createdAt": "2024-12-23T11:11:48.943000",
      "updatedAt": "2024-12-23T11:11:48.943000"
    }
  ]
}
```

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
