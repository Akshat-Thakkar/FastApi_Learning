from app import route_blog
from fastapi import APIRouter
from app import route_login
router = APIRouter()
router.include_router(route_blog.router, prefix="", tags=[""], include_in_schema=False)
router.include_router(route_login.router, prefix="/auth", tags=[""], include_in_schema=False)
