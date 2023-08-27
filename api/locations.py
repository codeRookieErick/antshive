from fastapi import APIRouter
from common.http import value_or_not_found
from common.data import collection, create_record
from common.models import Location
from pymongo.collection import Collection

router = APIRouter(tags=["Locations"])

@router.get("/")
def get_locations():
    def get(locations:Collection):
        return [Location(**l) for l in locations.find()]
    return collection("locations", get)

@router.get("/{code}")
def get_location(code:str):
    def get(locations:Collection):
        result = value_or_not_found(locations.find({"code": code}))
        return Location(**result)
    return collection("locations", get)

@router.post("/")
def create_location(location:Location):
    def create(locations:Collection):
        document = create_record(location)
        locations.insert_one({**document})
        return document
    return collection("locations", create)
