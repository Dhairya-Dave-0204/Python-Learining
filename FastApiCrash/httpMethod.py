from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

demo_data = [
    {
        "id": 1,
        "title": "Charger",
        "price": 1000,
        "count": 10
    },
    {
        "id": 2,
        "title": "Headphones",
        "price": 3000,
        "count": 20
    },
    {
        "id": 3,
        "title": "Cover",
        "price": 100,
        "count": 50
    },
]

app = FastAPI()

class Product(BaseModel):
    id: int
    title: str
    price: float
    count: int = 1

products: List[Product] = demo_data

@app.get("/")
def get_root():
    return "Home page for the routes"

@app.get("/products")
def get_all_prod():
    return { "status": 200, "message": "Fetched product successfully", "data": products }


@app.post("/add-prod")
def add_product(data:Product):
    products.append(data)
    return { "status": 200, "message": "Added product successfully", "data": products }

@app.put("/update-prod/{prod_id}")
def update_prod(data:Product, prod_id:int):
    for index, item in enumerate(products):
        if item['id'] == prod_id:
            products[index] = data
            return { "status": 200, "message": "Updated product successfully", "data": products }
    else:
        return { "status": 400, "message": "Error in updating product / Failed to find one" }

@app.delete("/del-prod/{prod_id}")
def delete_prod(prod_id:int):
    for index, item in enumerate(products):
        if item.get("id") == prod_id:
            deleted = products.pop(index)
            return { "status": 200, "message": "Deleted product successfully", "data": deleted }
    else:
        { "status": 400, "message": "Error in updating product / Failed to find one" }