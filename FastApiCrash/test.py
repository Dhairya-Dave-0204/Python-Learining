# import fastapi
# print (fastapi.__version__)

from fastapi import FastAPI
from mockdata import products

app = FastAPI()

@app.get("/")
def home():
    return "Home page"

@app.get("/products")
def get_products():
    return products

#  Path parameters
@app.get("/products/path/{prod_id}")
def path_params(prod_id:int):
    for index, item in enumerate(products):
        print(f"Index: {index} \n Item: {item}")
        if item["id"] == prod_id:
            return item
    else:
        return "No item found"

#  Query params
@app.get("/products/path/")
def query_params(name:str):
    return {
        "greet": f"Hello {name}!"
    }