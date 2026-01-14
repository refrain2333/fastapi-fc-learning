from fastapi import FastAPI
from app.routers import tasks

def create_app() -> FastAPI:
    # 增加 root_path="/fc1"，这样 FastAPI 就能自动处理阿里云传来的 /fc1 前缀了
    app = FastAPI(title="FastAPI-FC-Debian12", root_path="/fc1")
    
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
