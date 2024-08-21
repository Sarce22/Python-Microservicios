from pydantic import BaseModel

class Phone(BaseModel):
    id: int
    name: str
    color: str
    year: str