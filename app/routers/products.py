from fastapi import APIRouter, HTTPException

from app.schemas import Product, ProductCreate

router = APIRouter(prefix="/products", tags=["products"])

products: list[Product] = []
next_id = 1


@router.get("/", response_model=list[Product])
def list_products():
    return products


@router.get("/{product_id}", response_model=Product)
def get_product(product_id: int):
    for p in products:
        if p.id == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")


@router.post("/", response_model=Product, status_code=201)
def create_product(data: ProductCreate):
    global next_id
    product = Product(id=next_id, **data.model_dump())
    next_id += 1
    products.append(product)
    return product


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):
    for p in products:
        if p.id == product_id:
            products.remove(p)
            return
    raise HTTPException(status_code=404, detail="Product not found")