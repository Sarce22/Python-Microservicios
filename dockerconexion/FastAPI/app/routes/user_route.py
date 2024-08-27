from fastapi import APIRouter, Body
from models.user import User

from database import UserModel

user_route = APIRouter()


# Obtener todos los usuarios
@user_route.get("/users")
def get_users():
    users = UserModel.select()
    return list(users.dicts())

@user_route.post("/users")
def create_user(user: User = Body(...)):
    UserModel.create(id=user.id,username=user.username, email=user.email, password=user.password)
    return user

# Obtener un usuario por ID
@user_route.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    user = UserModel.get(UserModel.id == user_id)
    return user

# Actualizar un usuario por ID
@user_route.put("/users/{user_id}")
def update_user(user_id: int, user: User = Body(...)):
    UserModel.update(id=user.id,username=user.username, email=user.email, password=user.password).where(UserModel.id == user_id).execute()
    return {"message": "User updated successfully"}

# Eliminar un usuario por ID
@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    UserModel.delete().where(UserModel.id == user_id).execute()
    return {"message": "User deleted successfully"}
