import os
import sys
import json

# 确保路径正确
root = "/code"
lib_path = os.path.join(root, "python")
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)
if root not in sys.path:
    sys.path.insert(0, root)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI(title="FastAPI-FC")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    @app.get("/")
    def root_node():
        return {"message": "Hello from Native Python 3.12!", "status": "success"}

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    try:
        from app.routers import tasks
        app.include_router(tasks.router)
    except Exception as e:
        print(f"Router import error: {e}")
        
    return app

app = create_app()

def handler(event, context):
    try:
        from mangum import Mangum
        # Mangum 适配
        adapter = Mangum(app, lifespan="off")
        
        # 处理 event 格式
        if isinstance(event, (bytes, bytearray)):
            event = json.loads(event.decode('utf-8'))
        elif isinstance(event, str):
            event = json.loads(event)
            
        response = adapter(event, context)
        
        # 补全阿里云 FC 必需字段
        if isinstance(response, dict):
            if "isBase64Encoded" not in response:
                response["isBase64Encoded"] = False
        
        return response
    except Exception as e:
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e), "type": "GlobalHandlerError"})
        }
