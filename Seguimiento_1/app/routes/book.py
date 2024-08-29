from fastapi import APIRouter, Body
from ..models.book import Book

book_route = APIRouter()

@book_route.get("/")
async def get_all_books():
    try: 
        return {"message": f"All book data"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@book_route.get("/{book_id}")
async def get_book(book_id: int):
    try: 
        return {"message": f"Book data for ID {book_id}"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@book_route.post("/")
async def create_book(book: Book = Body(...)):
    try: 
        return {"message": "Book created", "book": book}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@book_route.put("/{book_id}")
async def update_book(book_id: int, book: Book = Body(...)):
    try: 
        return {"message": f"Book with ID {book_id} updated", "book": book}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@book_route.delete("/{book_id}")
async def delete_book(book_id: int):
    try: 
        return {"message": f"Book with ID {book_id} deleted"}
    except Exception as e:
        print(e)
        return {"error":str(e)}