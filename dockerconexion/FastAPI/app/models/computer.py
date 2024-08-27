from pydantic import BaseModel

class Computer(BaseModel):
    id: int
    name: str
    description: str
    ram: int
    cpu: str