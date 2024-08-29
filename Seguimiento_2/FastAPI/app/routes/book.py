from fastapi import APIRouter, Body
from models.book import Book

from database import BookModel

book_route = APIRouter()

@book_route.get("/books")
def get_all_books():
    books = list(BookModel.select().dicts())
    return books


@book_route.get("/books/{book_id}")
def get_book(book_id: int):
    try:
        book = BookModel.get(BookModel.id == book_id)
        return book
    except Exception as e:
        print(e)
        return {"error": str(e)}

@book_route.post("/books")
def create_book(book: Book = Body(...)):
    new_book = BookModel.create(
        isbn=book.isbn,
        title=book.title,
        author=book.author,
        genre=book.genre,
        year_published=book.year_published
    )
    return new_book

@book_route.put("/books/{book_id}")
def update_book(book_id: int, book_data: Book = Body(...)):
    try:
        book = BookModel.get(BookModel.id == book_id)
        book.isbn = book_data.isbn
        book.title = book_data.title
        book.author = book_data.author
        book.genre = book_data.genre
        book.year_published = book_data.year_published
        book.save()
        return book
    except Exception as e:
        print(e)
        return {"error":str(e)}
    

@book_route.delete("/{book_id}")
def delete_book(book_id: int):
    try:
        book = BookModel.get(BookModel.id == book_id)
        book.delete_instance()
        return {"message": "Book deleted successfully"} 
    except Exception as e:
        print(e)
        return {"error":str(e)}   