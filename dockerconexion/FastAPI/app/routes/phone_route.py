from fastapi import APIRouter, Body
from models.phone import Phone

from database import PhoneModel

phone_route = APIRouter()


@phone_route.get("/phones")
def get_phones():
    phones = PhoneModel.select()
    return list(phones.dicts())


@phone_route.get("/phones/{phone_id}")
def get_phone_by_id(phone_id: int):
    phone = PhoneModel.get(PhoneModel.id == phone_id)
    return phone

@phone_route.post("/phones")
def create_phone(phone: Phone = Body(...)):
    PhoneModel.create(id=phone.id,name=phone.name, color=phone.color, year=phone.year)
    return phone


@phone_route.put("/phones/{phone_id}")
def update_phone(phone_id: int, phone: Phone = Body(...)):
    PhoneModel.update(id=phone.id,name=phone.name, color=phone.color, year=phone.year).where(PhoneModel.id == phone_id).execute()
    return {"message": "Phone updated successfully"}

@phone_route.delete("/phones/{phone_id}")
def delete_phone(phone_id: int):
    PhoneModel.delete().where(PhoneModel.id == phone_id).execute()
    return {"message": "Phone deleted successfully"}