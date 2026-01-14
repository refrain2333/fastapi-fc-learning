from fastapi import FastAPI
from app.routers import tasks

def create_app() -> FastAPI:
    app = FastAPI(
        title="FC Learning API",
        version="1.0.0"
    )

    @app.get("/", tags=["Root"])
    def read_root():
        return {
            "message": "Hello from FastAPI in Docker!",
            "runtime": "Custom Container (Python 3.12)"
        }

    app.include_router(tasks.router)
    return app

app = create_app()
