from fastapi import APIRouter, Body
from models.computer import Computer

from database import ComputerModel

computer_route = APIRouter()


@computer_route.get("/computers")
def get_computers():
    computers = ComputerModel.select()
    return list(computers.dicts())


@computer_route.post("/computers")
def create_computer(computer: Computer = Body(...)):
    ComputerModel.create(id=computer.id, name=computer.name, description=computer.description, ram=computer.ram, cpu=computer.cpu)
    return computer


@computer_route.put("/computers/{computer_id}")
def update_computer(computer_id: int, computer: Computer = Body(...)):
    ComputerModel.update(id=computer.id, name=computer.name, description=computer.description, ram=computer.ram, cpu=computer.cpu).where(ComputerModel.id == computer_id).execute()
    return {"message": "Computer updated successfully"}


@computer_route.delete("/computers/{computer_id}")
def delete_computer(computer_id: int):
    ComputerModel.delete().where(ComputerModel.id == computer_id).execute()
    return {"message": "Computer deleted successfully"}


@computer_route.get("/computers/{computer_id}")
def get_computer_by_id(computer_id: int):
    computer = ComputerModel.get(ComputerModel.id == computer_id)
    return computer


