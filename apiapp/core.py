from fastapi import FastAPI, security, HTTPException
from database import ENGINE, session
from order_router import orders_router
from product_router import products_router
# from schemas import JWTModel
# from fastapi_jwt_auth import AuthJWT


Session = session(bind=ENGINE)
app = FastAPI()


# @AuthJWT.load_config
# def config():
#     return JWTModel()


app.include_router(orders_router)
app.include_router(products_router)


@app.get("/")
async def landing():
    return "landing page"
