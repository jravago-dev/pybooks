from fastapi import APIRouter
from apis.v1 import route_member
from apis.v1 import route_book

api_router = APIRouter()

api_router.include_router(route_member.router,prefix="/members", tags=["members"])
api_router.include_router(route_book.router,prefix="/books", tags=["books"])