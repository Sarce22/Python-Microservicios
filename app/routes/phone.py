from fastapi import APIRouter, Body
from ..schemas.phone_shema import Phone

phone_route = APIRouter()

@phone_route.post("/")
def create_phone(phone: Phone = Body(...)):
    try:
        return phone
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@phone_route.get("/")
def get_phones():
    try:
        return []
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@phone_route.get("/{phone_id}")
def get_phone(phone_id: int):
    try:
        return phone_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@phone_route.put("/{phone_id}")
def update_phone(phone_id: int, phone: Phone = Body(...)):
    try:
        return phone
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@phone_route.delete("/{phone_id}")
def delete_phone(phone_id: int):
    try:
        return phone_id
    except Exception as e:
        print(e)
        return {"error":str(e)}    