from pydantic import BaseModel

class VideoGame(BaseModel):
    id: int
    name: str
    release_date: str
    platform: str
    genre: str
    publisher: str
    developer: str
    user_score: float
    total_sales: float
    critic_count: int
    user_count: int