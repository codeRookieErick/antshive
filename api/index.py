from fastapi import FastAPI
from products import router

api:FastAPI = FastAPI()

api.include_router(router, prefix="/products")

@api.get('/')
def home():
    return 'active'