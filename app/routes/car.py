from fastapi import APIRouter,Body
from ..schemas.car_shema import Car

car_route = APIRouter()

@car_route.post("/")
async def create_car(car:Car = Body(...)):
    try:
        return car
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@car_route.get("/")
async def get_all_cars():
    try:
        return {"cars":[]}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@car_route.get("/{car_id}")
async def get_car(car_id:int):
    try:
        return {"car":car_id}
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@car_route.put("/{car_id}")
async def update_car(car_id:int,car:Car = Body(...)):
    try:
        return {"car":car_id}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@car_route.delete("/{car_id}")
async def delete_car(car_id:int):
    try:
        return {"car":car_id}
    except Exception as e:
        print(e)
        return {"error":str(e)}
