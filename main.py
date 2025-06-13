from fastapi import FastAPI
from core.config import settings
from apis.base import Api_router
from app.base import router
from fastapi.staticfiles import StaticFiles

def include_router(app):
    app.include_router(Api_router)
    app.include_router(router)
    return app

def configure_static_files(app):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    configure_static_files(app)
    return app

app = start_application()

# @app.get("/")
# def hello():
#     return {"Hello": "fastapi"}
