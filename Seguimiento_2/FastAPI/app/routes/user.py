from fastapi import APIRouter, Body
from models.user import User

from database import UserModel

user_route = APIRouter()

@user_route.get("/users")
def get_users():
    users = list(UserModel.select().dicts())
    return users


@user_route.get("/users/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}



@user_route.post("/users")
def create_user(user: User = Body(...)):
    new_user = UserModel.create(
        username=user.username,
        email=user.email,
        password=user.password
    )
    return new_user


@user_route.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    try:
        user = UserModel.get(UserModel.id == user_id)
        user.username = user_data.get("username", user.username)
        user.email = user_data.get("email", user.email)
        user.password = user_data.get("password", user.password)
        user.save()
        return user
    except Exception as e:
        print(e)
        return {"error": str(e)}


@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        user.delete_instance()
        return {"message": "User deleted successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}