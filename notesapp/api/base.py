from fastapi import APIRouter
from api import route_note


api_router = APIRouter()
api_router.include_router(route_note.router, prefix="", tags=["note"])
