import uvicorn
from app.main import app

if __name__ == "__main__":
    # 容器内部直接启动
    uvicorn.run(app, host="0.0.0.0", port=9000)
