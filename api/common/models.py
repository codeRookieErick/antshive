from pydantic import BaseModel

class Code(BaseModel):
    code: str

class Product(BaseModel):
    name: str
    description: str
    unit_volume: float
    unit_weight: float

class ProductRecord(Code, Product):
    pass

class Location(BaseModel):
    name: str
    latitude: float
    longitude: float
    features: list[str]