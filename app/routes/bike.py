from fastapi import APIRouter, Body
from ..schemas.bike_shema import Bike

bike_route = APIRouter()

@bike_route.post("/")
def create_bike(bike: Bike = Body(...)):
    try:
        return bike
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@bike_route.get("/")
def get_bikes():
    try:
        return []
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@bike_route.get("/{bike_id}")
def get_bike(bike_id: int):
    try:
        return bike_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@bike_route.put("/{bike_id}")
def update_bike(bike_id: int, bike: Bike = Body(...)):
    try:
        return bike
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@bike_route.delete("/{bike_id}")
def delete_bike(bike_id: int):
    try:
        return bike_id
    except Exception as e:
        print(e)
        return {"error":str(e)}