from pydantic import BaseModel

class Plane(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    color: str