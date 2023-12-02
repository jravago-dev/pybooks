from fastapi import FastAPI
from core.config import settings


def start_app():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app


app = start_app()


@app.get("/")
def hello() -> dict[str, str]:
    return {"msg": "Hello FastAPI!"}
