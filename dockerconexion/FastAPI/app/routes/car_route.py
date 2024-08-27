from fastapi import APIRouter, Body
from models.car import Car

from database import CarModel

car_route = APIRouter()


@car_route.get("/cars")
def get_cars():
    cars = CarModel.select()
    return list(cars.dicts())


@car_route.post("/cars")
def create_car(car: Car = Body(...)):
    CarModel.create(id=car.id,brand=car.brand, model=car.model, year=car.year, color=car.color)
    return car


@car_route.get("/cars/{car_id}")
def get_car_by_id(car_id: int):
    car = CarModel.get(CarModel.id == car_id)
    return car


@car_route.put("/cars/{car_id}")
def update_car(car_id: int, car: Car = Body(...)):
    CarModel.update(id=car.id,brand=car.brand, model=car.model, year=car.year, color=car.color).where(CarModel.id == car_id).execute()
    return {"message": "Car updated successfully"}


@car_route.delete("/cars/{car_id}")
def delete_car(car_id: int):
    CarModel.delete().where(CarModel.id == car_id).execute()
    return {"message": "Car deleted successfully"}