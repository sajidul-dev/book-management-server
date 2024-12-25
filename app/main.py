from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.book_routes import router as book_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router, prefix="/api/v1", tags=["Books"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Book Management API"}
