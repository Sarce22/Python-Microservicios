from fastapi import APIRouter, Body
from ..schemas.user_shema import User

user_route = APIRouter()

@user_route.post("/")
def create_user(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@user_route.get("/")
def get_user():
    try:
        return []
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@user_route.get("/{user_id}")
def get_user(user_id: int):
    try:
        return user_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@user_route.put("/{user_id}")
def update_user(user_id: int, user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        return user_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
