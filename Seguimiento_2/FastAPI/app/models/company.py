from pydantic import BaseModel

class Company(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    phone_number: str
    email: str
    website: str