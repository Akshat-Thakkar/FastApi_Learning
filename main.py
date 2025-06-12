from fastapi import FastAPI
from core.config import settings
from apis.base import router

def include_router(app):
    app.include_router(router)
    return app


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app = start_application()

@app.get("/")
def hello():
    return {"Hello": "fastapi"}
