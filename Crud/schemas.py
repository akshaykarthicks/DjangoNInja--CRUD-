from ninja import Schema 
from typing import Optional #optional is used to make the field optional


class ItemCreateSchema(Schema):
    name:str
    description:Optional[str]=None
    price:float

class ItemUpdateSchema(Schema):
    name:Optional[str]=None
    description:Optional[str]=None
    price:Optional[float]=None

class ItemOutSchema(Schema):
    id:int
    name:str
    description:Optional[str]=None
    price:float

