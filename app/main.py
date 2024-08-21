from fastapi import FastAPI
from starlette.responses import RedirectResponse

# app routes

from .routes.user import user_route
from .routes.car import car_route
from .routes.bike import bike_route
from .routes.phone import phone_route
from .routes.computer import computer_route
from .routes.plane import plane_route


app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")


#---Usuarios---#
app.include_router(user_route, prefix="/users", tags=["Usuarios"])

#--- carros---#
app.include_router(car_route, prefix="/cars", tags=["Carros"])

#--- bikes---#
app.include_router(bike_route, prefix="/bikes", tags=["Bikes"])

#---phone---#
app.include_router(phone_route, prefix="/phones", tags=["Phones"])

#---computer---#
app.include_router(computer_route, prefix="/computers", tags=["Computers"])

#----Plane---#
app.include_router(plane_route, prefix="/planes", tags=["Planes"])