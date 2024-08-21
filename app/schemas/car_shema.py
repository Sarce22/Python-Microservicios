from pydantic import BaseModel

class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str