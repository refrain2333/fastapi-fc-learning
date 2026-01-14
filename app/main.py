import os
import sys
import json

# 路径注入
root = "/code"
lib_path = os.path.join(root, "python")
if lib_path not in sys.path:
    sys.path.insert(0, lib_path)
if root not in sys.path:
    sys.path.insert(0, root)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    # 保持 root_path="/fc1" 以适配你的自定义域名路径
    app = FastAPI(title="FastAPI-FC-312", root_path="/fc1")
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/")
    def read_root():
        return {
            "message": "Success! Running on Native Python 3.12",
            "runtime": "Standard python3.12 Runtime",
            "info": "Based on Debian (Native)"
        }

    @app.get("/ping")
    def ping():
        return {"ping": "pong"}

    return app

app = create_app()

def handler(event, context):
    try:
        from mangum import Mangum
        # 兼容性处理：阿里云 event 可能是字典、字符串或字节流
        if isinstance(event, (bytes, bytearray)):
            event = json.loads(event.decode('utf-8'))
        elif isinstance(event, str):
            event = json.loads(event)
            
        adapter = Mangum(app, lifespan="off")
        response = adapter(event, context)
        
        # 补全关键字段，防止 ERR_INVALID_RESPONSE
        if isinstance(response, dict):
            if "isBase64Encoded" not in response:
                response["isBase64Encoded"] = False
        
        return response
    except Exception as e:
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e), "type": "Native312HandlerError"})
        }
