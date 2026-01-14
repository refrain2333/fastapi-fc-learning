from fastapi import FastAPI
from app.routers import tasks

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI-FC-Debian12")
    
    @app.get("/")
    def read_root():
        return {
            "message": "Success! Running on Debian 12 (Python 3.11)",
            "mode": "Custom Runtime (Web Server)"
        }

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    app.include_router(tasks.router)
    return app

app = create_app()
