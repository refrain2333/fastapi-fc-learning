# 使用官方 Python 3.12 轻量镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /code

# 设置环境变量，确保 Python 输出直接打印到日志，不被缓存
ENV PYTHONUNBUFFERED=1

# 复制依赖清单（利用 Docker 缓存层）
COPY requirements.txt .

# 安装依赖
# 使用阿里云镜像源加快下载速度
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 复制项目所有代码到镜像中
COPY . .

# 暴露 FastAPI 运行的端口
EXPOSE 9000

# 启动命令
# 注意：在容器中直接运行 python main.py 即可
CMD ["python", "main.py"]
