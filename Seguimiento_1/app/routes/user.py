from fastapi import APIRouter, Body
from ..models.user import User

user_route = APIRouter()

@user_route.get("/")
async def get_all_users():
    try: 
        
        return {"message": f"All user data"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@user_route.get("/{user_id}")
async def get_user(user_id: int):
    try: 
        return {"message": f"User data for ID {user_id}"}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@user_route.post("/")
async def create_user(user: User = Body(...)):
    try: 
        return {"message": "User created", "user": user}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@user_route.put("/{user_id}")
async def update_user(user_id: int, user: User = Body(...)):
    try: 
        return {"message": f"User with ID {user_id} updated", "user": user}
    except Exception as e:
        print(e)
        return {"error":str(e)}

@user_route.delete("/{user_id}")
async def delete_user(user_id: int):
    try: 
        return {"message": f"User with ID {user_id} deleted"}
    except Exception as e:
        print(e)
        return {"error":str(e)}