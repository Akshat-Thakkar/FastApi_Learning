from fastapi import APIRouter
from apis import route_user
from apis import route_blog
from apis import route_login

Api_router = APIRouter()
Api_router.include_router(route_user.router, prefix="/users", tags=["users"])
Api_router.include_router(route_blog.router, prefix="/blogs", tags=["blogs"])
Api_router.include_router(route_login.router, prefix="", tags=["login"])