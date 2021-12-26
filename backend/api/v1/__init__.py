from fastapi import APIRouter
from api.v1.Items import items as items_router


routes = APIRouter()

routes.include_router(items_router)