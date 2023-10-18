# create a FastAPI app that returns 5 products at unique endpoints, each url should be a random string

from fastapi import FastAPI
import random
from pydantic import BaseModel
from typing import List, Union

app = FastAPI()

# create a python class for product with the fields product_id, name, description, and price

class Product(BaseModel):
    id: int
    description: str 
    price: float
    tax: float
    tags: List[str] = []


product_list = [
    Product(id=12345789, description="This is product 1", price=10.0, tax=0.7, tags=["tag1", "tag2"]),
    Product(id=987654321, description="This is product 2", price=20, tax=0.7) 
    ]
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/products/{product_id}")
def read_item(product_id: int, q: str = None):
    for product in product_list:
        if product.id == product_id:
            return product
    else:
        return {"Not": "Found"}
    
@app.post("/products/")
def create_product(product: Product):
    product_list.append(product)
    return product