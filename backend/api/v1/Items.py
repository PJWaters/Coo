from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from db import db
from models.Items import ItemModel

items = APIRouter(prefix="/items", tags=["items"])

@items.post("/", response_model=ItemModel)
async def create_item(item: ItemModel = Body(...)):
    item = jsonable_encoder(item)
    new_item = await db.items.insert_one(item)
    created_item = await db.items.find_one({"_id": new_item.inserted_id})
    return JSONResponse(status_code= status.HTTP_201_CREATED, content=created_item)

@items.get("/", response_description="List all items", response_model=List[ItemModel])
async def list_items():
    items = await db.items.find().to_list(1000)
    return items