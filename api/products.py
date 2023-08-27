from fastapi import APIRouter
from common.data import connection, collection, create_record
from common.models import Product, ProductRecord
from common.http import value_or_not_found
from pymongo.collection import Collection
import uuid

router = APIRouter(tags=["Products"])

@router.get("/")
def get_products():
    def get(products:Collection):
        return [ProductRecord(**i) for i in products.find()]
    return collection("products", get)

@router.get("/{code}")
def get_product_with_code(code:str):
    def get(products:Collection):
        result = value_or_not_found(products.find_one({"code": code}))
        return ProductRecord(**result)
    return collection("products", get)

@router.post("/")
def create_product(product:Product):
    def create(col:Collection):
        document = create_record(product)
        col.insert_one({**document})
        return document
    return collection("products", create)