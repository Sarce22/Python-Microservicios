from pydantic import BaseModel

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: float