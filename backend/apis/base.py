from fastapi import APIRouter
from apis.v1 import route_member

api_router = APIRouter()

api_router.include_router(route_member.router,prefix="/members", tags=["members"])