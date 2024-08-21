from fastapi import APIRouter, Body
from ..schemas.computer_shema import Computer

computer_route = APIRouter()

@computer_route.post("/")
def create_computer(computer: Computer = Body(...)):
    try:
        return computer
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@computer_route.get("/")
def get_computers():
    try:
        return []
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@computer_route.get("/{computer_id}")
def get_computer(computer_id: int):
    try:
        return computer_id
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@computer_route.put("/{computer_id}")
def update_computer(computer_id: int, computer: Computer = Body(...)):
    try:
        return computer
    except Exception as e:
        print(e)
        return {"error":str(e)}
    
@computer_route.delete("/{computer_id}")
def delete_computer(computer_id: int):
    try:
        return computer_id
    except Exception as e:
        print(e)
        return {"error":str(e)}    