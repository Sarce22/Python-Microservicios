from fastapi import FastAPI
from starlette.responses import RedirectResponse

# Base de datos
from database import database as connection
from routes.user_route import user_route
from routes.car_route import car_route
from routes.phone_route import phone_route
from routes.bike_route import bike_route
from routes.computer_route import computer_route
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/api/users", tags=["users"])


app.include_router(car_route, prefix="/api/cars", tags=["cars"])


app.include_router(phone_route, prefix="/api/phones", tags=["phones"])


app.include_router(bike_route, prefix="/api/bikes", tags=["bikes"])


app.include_router(computer_route, prefix="/api/computers", tags=["computers"])



