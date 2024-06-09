from fastapi import APIRouter

products_router = APIRouter(prefix='/products')


@products_router.get("/")
async def get_products():
    return {"message": "product page"}
