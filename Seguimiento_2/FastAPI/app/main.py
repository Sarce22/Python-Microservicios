from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from database import database as connection
from routes.user import user_route
from routes.book import book_route
from routes.order import order_route
from routes.company import company_route
from routes.videoGame import video_game_route

from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    if connection.is_closed():
        connection.connect()
    try:
        yield  
    finally:
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/api/users", tags=["Users"])
app.include_router(book_route, prefix="/api/book", tags=["Book"])
app.include_router(company_route, prefix="/api/company", tags=["Company"])
app.include_router(order_route,prefix="/api/order", tags=["Order"])
app.include_router(video_game_route, prefix="/api/videoGame", tags=["VideoGame"])