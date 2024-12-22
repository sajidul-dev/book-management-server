import os

class Settings:
    MONGODB_URI: str = os.getenv("MONGODB_URI", "mongodb+srv://university-management-system:university-management-system@cluster0.nugvpbs.mongodb.net/book-management?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "book_db")

settings = Settings()
