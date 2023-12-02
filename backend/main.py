from fastapi import FastAPI
from core.config import settings
from apis.base import api_router

def include_router(app):
    app.include_router(api_router)

def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app


app = start_app()


@app.get("/")
def hello() -> dict[str, str]:
    return {"msg": "Hello FastAPI!"}
