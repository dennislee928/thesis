# 使用官方的 Python 基礎映像
FROM python:3.14.0rc1-slim

# 設定工作目錄
WORKDIR /app

# 安裝必要的系統工具
RUN apt-get update && apt-get install -y g++ && rm -rf /var/lib/apt/lists/*

# 複製當前目錄下的所有文件到容器的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip install --no-cache-dir qutip numpy matplotlib

# 設定容器啟動時執行的命令
CMD ["python", "blackhole_simulation.py"]
