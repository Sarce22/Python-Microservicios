from fastapi import APIRouter, Body
from ..schemas.plane_shema import Plane

plane_route = APIRouter()


@plane_route.post("/")
def create_plane(plane: Plane = Body(...)):
    try:
        return plane
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@plane_route.get("/")
def get_planes():
    try:
        return []
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@plane_route.get("/{plane_id}")
def get_plane(plane_id: int):
    try:
        return plane_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@plane_route.put("/{plane_id}")
def update_plane(plane_id: int, plane: Plane = Body(...)):
    try:
        return plane
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@plane_route.delete("/{plane_id}")
def delete_plane(plane_id: int):
    try:
        return plane_id
    except Exception as e:
        print(e)
        return {"error":str(e)}    