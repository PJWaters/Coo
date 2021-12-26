from fastapi import APIRouter
import api.v1 as v1

routes = APIRouter()
routes.include_router(v1.routes, prefix="/v1")