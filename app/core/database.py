from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGODB_URI)
database = client[settings.DATABASE_NAME]
books_collection = database["books"]
