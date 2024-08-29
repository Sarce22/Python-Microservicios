from fastapi import APIRouter, Body
from models.order import Order


from database import OrderModel
order_route = APIRouter()

@order_route.get("/orders")
def get_all_orders():
    orders = list(OrderModel.select().dicts())
    return orders

@order_route.get("/orders/{order_id}")
def get_order(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        return order
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.post("/orders")
def create_order(order: Order = Body(...)):
    new_order = OrderModel.create(
        user_id=order.user_id,
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=order.total_price
    )
    return new_order


@order_route.put("/orders/{order_id}")
def update_order(order_id: int, order_data: Order = Body(...)):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        order.user_id = order_data.user_id
        order.product_id = order_data.product_id
        order.quantity = order_data.quantity
        order.total_price = order_data.total_price
        order.save()
        return order
    except Exception as e:
        print(e)
        return {"error": str(e)}

@order_route.delete("/orders/{order_id}")
def delete_order(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        order.delete_instance()
        return {"message": "Order deleted successfully"}
    except Exception as e:
        print(e)
        return {"error": str(e)}