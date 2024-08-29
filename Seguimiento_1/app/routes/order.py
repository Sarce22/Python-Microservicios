from fastapi import APIRouter, Body
from ..models.order import Order

order_route = APIRouter()

@order_route.get("/")
async def get_all_orders():
    try: 
        return {"message": "All order data"}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.get("/{order_id}")
async def get_order(order_id: int):
    try: 
        return {"message": f"Order data for ID {order_id}"}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.post("/")
async def create_order(order: Order = Body(...)):
    try: 
        return {"message": "Order created", "order": order}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.put("/{order_id}")
async def update_order(order_id: int, order: Order = Body(...)):
    try: 
        return {"message": f"Order with ID {order_id} updated", "order": order}
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.delete("/{order_id}")
async def delete_order(order_id: int):
    try: 
        return {"message": f"Order with ID {order_id} deleted"}
    except Exception as e:
        print(e)
        return {"error": str(e)}
