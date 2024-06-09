from pydantic import BaseModel
from typer import Option


class LoginModel(BaseModel):
    username: str
    password: str


class RegisterModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    password: str
    is_active: bool
    is_superuser: bool


class OrderModel(BaseModel):
    id: int
    product_id: int
    user_id: int
    count: int
    order_status: str


class CategoryModel(BaseModel):
    id: int
    name: str


class ProductModel(BaseModel):
    id: int
    name: str
    description: str
    count: int
    price: float


class SWTModel(BaseModel):
    authjwt_secret_key: str = 'd8d5caf1c6b69305528e79caa80f1c7b8fd3e17038e2e654c213a4d893d04359'
