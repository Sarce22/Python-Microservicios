from fastapi import APIRouter, Body
from models.bike import Bike

from database import BikeModel

bike_route = APIRouter()


@bike_route.get("/bikes")
def get_bikes():
    bikes = BikeModel.select()
    return list(bikes.dicts())


@bike_route.post("/bikes")
def create_bike(bike: Bike = Body(...)):
    BikeModel.create(id=bike.id,brand=bike.brand, model=bike.model, year=bike.year, color=bike.color)
    return bike


@bike_route.put("/bikes/{bike_id}")
def update_bike(bike_id: int, bike: Bike = Body(...)):
    BikeModel.update(id=bike.id,brand=bike.brand, model=bike.model, year=bike.year, color=bike.color).where(BikeModel.id == bike_id).execute()
    return {"message": "Bike updated successfully"}


@bike_route.delete("/bikes/{bike_id}")  
def delete_bike(bike_id: int):
    BikeModel.delete().where(BikeModel.id == bike_id).execute()
    return {"message": "Bike deleted successfully"}

@bike_route.get("/bikes/{bike_id}")
def get_bike_by_id(bike_id: int):
    bike = BikeModel.get(BikeModel.id == bike_id)
    return bike