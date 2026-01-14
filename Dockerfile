# 使用官方 Python 3.12 镜像，其底座是 Debian 12 (Bookworm)
FROM python:3.12-slim-bookworm

# 设置工作目录
WORKDIR /code

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 复制依赖清单
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 复制所有代码
COPY . .

# 暴露端口
EXPOSE 9000

# 启动命令
CMD ["python", "main.py"]
