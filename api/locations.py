from fastapi import APIRouter
from common.data import connection, collection
from common.models import Product
from pymongo.database import Database
from pymongo.collection import Collection
import uuid

router = APIRouter()

def get_products_from_database(database:Database):
    products = database["products"]
    return [i for i in products.find()]

@router.get("/")
def get_products():
    return connection(get_products_from_database)

@router.post("/")
def create_product(product:Product):
    def create(col:Collection):
        document = {**dict(product), "code": str(uuid.uuid4())}
        print(col.insert_one({**document}))
        return document
    return collection("products", create)
    
        