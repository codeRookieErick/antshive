from typing import TypeVar
from fastapi.exceptions import HTTPException

def not_success(status_code:int, detail:str = None):
    raise HTTPException(status_code, detail or 'Bobo')

def not_found(detail:str = None):
    return not_success(404, detail)

T = TypeVar("T")
def value_or_not_found(value:T) -> T|None:
    return value or not_found()