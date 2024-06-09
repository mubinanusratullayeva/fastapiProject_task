from fastapi import APIRouter

orders_router = APIRouter(prefix='/orders')


@orders_router.get("/")
async def get_orders():
    return {"message": "order page"}
