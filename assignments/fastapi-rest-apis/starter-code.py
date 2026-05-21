from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Book API")


# In-memory sample data for the assignment.
books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "Automate the Boring Stuff", "author": "Al Sweigart", "year": 2015},
]


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API assignment"}


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(new_book: BookCreate):
    next_id = max((book["id"] for book in books), default=0) + 1
    created = {
        "id": next_id,
        "title": new_book.title,
        "author": new_book.author,
        "year": new_book.year,
    }
    books.append(created)
    return created