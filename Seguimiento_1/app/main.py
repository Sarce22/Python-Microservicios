from fastapi import FastAPI
from starlette.responses import RedirectResponse

#Routes
from .routes.user import user_route
from .routes.book import book_route
from .routes.company import company_route
from .routes.order import order_route
from .routes.videoGame import video_game_route

app = FastAPI()

#Routes
app.include_router(user_route, prefix="/user", tags=["user"])
app.include_router(book_route, prefix="/book", tags=["book"])
app.include_router(company_route, prefix="/company", tags=["company"])
app.include_router(order_route,prefix="/order", tags=["order"])
app.include_router(video_game_route, prefix="/videoGame", tags=["videoGame"])

#Documentation
@app.get("/")
async def read_root():
    return RedirectResponse(url="/docs")

