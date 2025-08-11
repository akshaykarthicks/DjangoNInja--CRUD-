from ninja import NinjaAPI, Schema
from ninja.security import HttpBearer
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from typing import List
from .models import Item, Token
from .schemas import ItemCreateSchema, ItemUpdateSchema, ItemOutSchema
from django.contrib.auth.models import User

api=NinjaAPI(title="CRUD API",description="A simple CRUD API for items")

# Django Ninja authentication class
class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            token = Token.objects.get(key=token)
            request.user = token.user
            return token
        except Token.DoesNotExist:
            return None

class LoginSchema(Schema):
    username: str
    password: str

@api.post("/login")
def login(request, payload: LoginSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return {"token": token.key}
    else:
        return {"error": "Invalid credentials"}, 401

def item_to_schema(item:Item)->ItemOutSchema:
    return ItemOutSchema(
        id=item.id,
        name=item.name,
        description=item.description,
        price=item.price
    )

#Create Item api
@api.post("/items",response=ItemOutSchema,auth=AuthBearer())
def create_item(request:HttpRequest,payload:ItemCreateSchema): # pay load The body of the POST request, automatically parsed & validated against 
    try:
        item=Item.objects.create(
            name=payload.name,
            description=payload.description,
            price=payload.price
        )
        return item_to_schema(item)
    except Exception as e:
        return {"error": str(e)}, 500


#update item api
@api.put("/items/{item_id}",response=ItemOutSchema,auth=AuthBearer())
def update_item(request:HttpRequest,item_id:int,payload:ItemUpdateSchema):
    item=get_object_or_404(Item,id=item_id)

    if payload.name is not None:
        item.name=payload.name
    if payload.description is not None:
        item.description=payload.description
    if payload.price is not None:
        item.price=payload.price

    item.save()
    return item_to_schema(item)


#delete item api

@api.delete("/items/{item_id}",auth=AuthBearer())
def delete_item(request:HttpRequest,item_id:int):
    item=get_object_or_404(Item,id=item_id)
    item.delete()
    return {"message":"Item deleted successfully"}

# READ: List all items
@api.get("/items", response=List[ItemOutSchema])
def list_items(request: HttpRequest, limit: int = 10, offset: int = 0):
    """List all items with pagination"""
    items = Item.objects.all()[offset:offset + limit]
    return [item_to_schema(item) for item in items]

# READ: Get single item
@api.get("/items/{item_id}", response=ItemOutSchema)
def get_item(request: HttpRequest, item_id: int):
    item = get_object_or_404(Item, id=item_id)
    return item_to_schema(item)