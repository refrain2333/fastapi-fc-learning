from fastapi import FastAPI
from app.routers import tasks

def create_app() -> FastAPI:
    app = FastAPI(
        title="FC Learning API",
        description="这是一个演示 FastAPI 功能的示例项目，用于学习如何部署到函数计算。",
        version="1.0.0"
    )

    @app.get("/", tags=["Root"])
    def read_root():
        return {
            "message": "欢迎使用阿里云函数计算上的 FastAPI (Python 3.12)!",
            "docs": "访问 /docs 查看接口文档"
        }

    app.include_router(tasks.router)
    
    return app

app = create_app()
