from pydantic import BaseModel

class Book(BaseModel):
    id: int
    isbn: int
    title: str
    author: str
    genre: str
    year_published: int