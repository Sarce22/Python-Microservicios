from pydantic import BaseModel

class Bike(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str