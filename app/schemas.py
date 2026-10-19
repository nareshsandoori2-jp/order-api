from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int = 0


class Product(ProductCreate):
    id: int